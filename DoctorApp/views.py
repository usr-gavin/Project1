from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from msrest import Serializer
from DoctorApp.Views.userview import RegisterView,LoginView,UserView,LogoutView
from DoctorApp.Views.patientview import PatientView,PatientEditView
from DoctorApp.Views.adminview import AdminView,AdminresView

#jws restframework
from rest_framework.views import APIView

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from DoctorApp.models import Patients
from DoctorApp.serializers import PatientSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def addpost(request):
    #return HttpResponse("hello")
    return render(request,"DoctorApp/addpost.html")


@csrf_exempt
def showpost(request):
    #return HttpResponse("hello")
    patients = Patients.objects.all()
    context={'patients':patients}
    return render(request,"DoctorApp/showpost.html",context)

@csrf_exempt
def signin(request):
    #return HttpResponse("hello")
    if request.method=='POST':
        uid = request.POST['uname']
        pas = request.POST['psw']

        user=authenticate(username=uid, password=pas)
        if user is not None:
            login(request,user)
            name=user.first_name
            return HttpResponse("Login Successfully")
        else:
            return HttpResponse("user not found") 
    else:
        return HttpResponse("function not found") 
                
@csrf_exempt
def homepage(request):
    #return HttpResponse("hello")
    return render(request,"DoctorApp/homepage.html")
   


   #rest jws

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import DoctorSerializer
from .models import Doctors

import jwt, datetime


# Create your views here. 



#for_patient



#Adminview

