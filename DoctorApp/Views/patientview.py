from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from DoctorApp.models import Doctors
from DoctorApp.models import Patients
from DoctorApp.serializers import DoctorSerializer
from DoctorApp.serializers import PatientSerializer


class PatientView(APIView):
    @csrf_exempt
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if token:
        
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            user = Doctors.objects.filter(id=payload['id']).first()                        
            patients = Patients.objects.filter(Con_Doc=user.name)
            serializer=PatientSerializer(patients,many=True)
            return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() #saving User profile
        return Response(serializer.data)

class PatientEditView(APIView):

    @csrf_exempt
    def put(self, request,*args, **kwargs):
        data=request.data        
        user = Patients.objects.get( _id =data["_id"])
        user.PatientName=data["PatientName"]
        #user.PatientImg=data["PatientImg"]
        #user.Con_Doc=data["Con_Doc"]
        #user.Diagnosis=data["Diagnosis"]
        #user=data
        user.save() 
        serializer=PatientSerializer(user)
        return Response(serializer.data)

