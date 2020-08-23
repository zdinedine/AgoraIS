from django.db import models

# Create your models here.
class Destination(models.Model):

    id = models.CharField(primary_key=True, max_length=20)
    img = models.ImageField(upload_to = 'pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
