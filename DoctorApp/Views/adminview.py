from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from DoctorApp.models import Doctors
from DoctorApp.serializers import DoctorSerializer

class AdminView(APIView):
    @csrf_exempt
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if token:
        
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])

            user = Doctors.objects.filter(isvalid="waiting")
            

            serializer=DoctorSerializer(user,many=True)
            
            return Response(serializer.data)

class AdminresView(APIView):
    @csrf_exempt
    def put(self, request,*args, **kwargs):
        data=request.data        
        user = Doctors.objects.get(isvalid="waiting" , id=data["id"])
        
        user.isvalid=data["isvalid"]
        user.save()
        serializer=DoctorSerializer(user)
        return Response(serializer.data)

