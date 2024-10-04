from django.contrib.auth import get_user_model
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length= 255, blank= False)
    model = models.CharField(max_length= 255, blank= False)
    year = models.PositiveIntegerField(blank= True, null= True)
    description = models.TextField(blank= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    owner = models.ForeignKey( 'auth.user', on_delete= models.CASCADE)


class Comment(models.Model):
    content = models.TextField(blank= False)
    created_at = models.DateTimeField(auto_now_add= True)

    car = models.ForeignKey('Car', on_delete= models.CASCADE)
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE)