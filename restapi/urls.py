from django.urls import path


from . import  views
from .views import home,employee,delete_employee,update_employee,LogoutView,LoginView,department
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    #  path('home/',home.as_view(),name='home'),
     path('user/',home.as_view(),name='users'),
     path('login/',LoginView.as_view(),name='LoginView'),
     path('logout/',LogoutView.as_view(),name='LogoutView'),
     path('department/',department.as_view(),name='department'),
     path('employee/',employee.as_view(),name='employee'),
     path('delete_employee/<int:id>',delete_employee.as_view(),name='delete_employee'),
     path('update_employee/<int:id>',update_employee.as_view(),name='update_employee')

]
