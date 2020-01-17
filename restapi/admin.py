from django.contrib import admin
from  .models import Employees,Department,Album,Track
# Register your models here.
admin.site.register(Employees)
admin.site.register(Department)
admin.site.register(Album)
admin.site.register(Track)


# def send_json(self,request):
#         department=Department.objects.all()
#         return JsonResponse(data, safe=False)