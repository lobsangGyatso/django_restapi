from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import employeeSerilizer,EmplopyeeSerializer,LoginSerializer,DepartmentSerilizer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .models import Employees,Department
from django.contrib.auth import authenticate,login as lg
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework.response import Response
from django.conf import settings
import jwt
import json
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication,BasicAuthentication
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token
from django.shortcuts import render,get_object_or_404
# Create your views here.


authentication_classes=[TokenAuthentication,SessionAuthentication, BasicAuthentication]
permission_classes=[IsAuthenticated]
class home(APIView):
    def get(self,request):
        obj=User.objects.all()
        serilizer= employeeSerilizer(obj,many=True)
        return Response(serilizer.data)
from rest_framework import viewsets 

class employee(APIView):
    #  queryset=Employees.objects.all()
    #  serializer_class=EmplopyeeSerializer
    def get(self,request):
        obj=Employees.objects.all()
        serilizer=EmplopyeeSerializer(obj,many=True)
        return Response(serilizer.data)


    def post(self,request,*args,**kwargs):
        print('............')
        data = request.data
        print(data)
        serializer = EmplopyeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class delete_employee(APIView):
    def get_object(self):
        obj=None;
        id=self.kwargs.get('id')
        print("id is",id)
        if id is not None:
            obj=Employee.objects.get(id=id)
        return obj

    def delete(self,request,id=None,*args,**kwargs):
        obj=self.get_object()
        if obj is not None:
           obj.delete()
        return Response({"success":"haha"})

class update_employee(APIView):
    def get_object(self):
        print("22222222222222222222222")
        obj=None
        id=self.kwargs.get('id')
        if id is not None:
            obj=Employee.objects.get(id=id)
        return obj
    
    def put(self, request, id=None):
        saved_article = self.get_object()
        data = request.data
        serializer = EmplopyeeSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid():
           article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully"})
# def logout(request):
#     def post(self, request, format=None):
#         # simply delete the token to force a login
#         request.logout()
#         return Response({"logout"},status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)

    # print("sdsdfsdfsdfsdfsdf")
    # def get(self,request):
    #     username = request.data['username']
       
    #     print("sasasas")
    #     print("wwwwwwwwwwwwwwww",username)
    #     password=request.data['password']
    #     user = authenticate(username=username,password=password)
    #     if user:
    #         try:
    #             payload=jwt_payload_handler(user)
    #             token=jwt.encode(payload,settings.SECRET_KEY)
    #             userDetails={}
    #             userDetails['username']=user.username
    #             userDetails['token']=token
    #             print(userDetails['token'])
    #             lg(request,user)
    #             return Response(userDetails,status=status.HTTP_200_OK)
    #         except Exception as e:
    #             raise e
    #     else:
    #         res={
    #             'error':'can not authenticate'
    #         }
    #     return Response(res)





class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)



class department(APIView):
    def get(self,request):
        department=Department.objects.all()
        serilizer=DepartmentSerilizer(department,many=True)
        return Response(serilizer.data)

