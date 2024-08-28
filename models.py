from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="picture/")
    
# class Files(models.Model):
#    file=  models.FileField(upload_to='file/')

