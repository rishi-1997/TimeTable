from django.db import models

# Create your models here.
class TimeTable(models.Model):
    time = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    topics = models.CharField(max_length=150)