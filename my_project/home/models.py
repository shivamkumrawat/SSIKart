from django.db import models


# Create your models here.
class category(models.Model):
 name =models.CharField(max_lenght=100, unique=True)
 slug= models.CharField(max_lenght=100, unique=True)
 description =models>TextField(max_lenght=255, blank=True,)
 image=models.ImageField(upload_to='img/categories', blank)

def_str_(self):
    return self.name