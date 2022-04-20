from rest_framework import serializers
from DoctorApp.models import Doctors, Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('PatientId','PatientName','PatientImg','Con_Doc','Diagnosis')



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = [ 'id','name', 'email', 'password','phone','address','specification']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
