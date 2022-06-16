import imp
from pickle import FROZENSET
from django.conf.urls import url
from django.urls import path, include
from DoctorApp import views
from .views import AdminView, AdminresView, RegisterView, LoginView,UserView,LogoutView,PatientView,PatientEditView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    
    path('addpost',views.addpost),

    path('showpost',views.showpost),


    path('register',RegisterView.as_view()),

    path('login',LoginView.as_view()),

    path('user',UserView.as_view()),

    path('logout',LogoutView.as_view()),

    path('patient',PatientView.as_view()),

    path('patientedit',PatientEditView.as_view()),

    path('admin',AdminView.as_view()),

    path('adminres',AdminresView.as_view()),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)