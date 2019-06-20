from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    Sendamessage=models.CharField(max_length=264)
