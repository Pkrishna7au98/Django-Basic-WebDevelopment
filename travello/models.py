from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics/djangopics')
    desc = models.TextField()
    price = models.IntegerField(default='450')
    offer = models.BooleanField(default=False)