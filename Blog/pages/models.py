from django.db import models

# Create your models here.
class Notee(models.Model):
    text = models.CharField(max_length=100)