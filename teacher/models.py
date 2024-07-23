from django.db import models

# Create your models here.
class Teacher_2():
    F_name = models.CharField(max_length=255,null=True)
    L_name = models.CharField(max_length=255,null=True)
    Address = models.CharField(max_length=200,null=False)
    phone = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.F_name}'