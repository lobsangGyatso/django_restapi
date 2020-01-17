from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedIdentityField
from .models import Employees,Department,Track,Album
from rest_framework import exceptions
from django.contrib.auth import authenticate


class employeeSerilizer(serializers.ModelSerializer): 
    class Meta:
      model  = User
      fields= '__all__'
class DepartmentSerilizer(serializers.ModelSerializer):
  
    class Meta:
        model =Department
        fields = '__all__'
       


class EmplopyeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employees
        fields = '__all__'
        depth=1

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']