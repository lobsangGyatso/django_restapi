from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=20)
    # location=models.CharField(max_length=20)
   
class Employees(models.Model):
    department=models.ForeignKey(Department, related_name='tracks', on_delete=models.CASCADE)
    name  = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age   = models.IntegerField()
    address = models.CharField(max_length=20)
   
    # def __str__(self):
    #     return Department



class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)