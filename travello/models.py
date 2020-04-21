from django.db import models

# Create your models here.
class Description(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'pics')
    offer = models.BooleanField(default = False)