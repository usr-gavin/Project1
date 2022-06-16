from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from DoctorApp.models import Doctors
from DoctorApp.serializers import DoctorSerializer
from rest_framework.exceptions import AuthenticationFailed

class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() #saving User profile
        return Response(serializer.data)


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Doctors.objects.filter(email=email).first()
            
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        if user.isvalid=="waiting":
            raise AuthenticationFailed('Waiting for Authorization')
        
        if user.isvalid=="denied":
            raise AuthenticationFailed("Sorry! your request is denied Please contact Administrator")
        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    @csrf_exempt
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Doctors.objects.filter(id=payload['id']).first()
        
        serializer = DoctorSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    @csrf_exempt
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
