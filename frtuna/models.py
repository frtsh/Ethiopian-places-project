from django.db import models

# Create your models here.

class Destinations(models.Model):
    
   # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics', blank=False, null=False)
    desc = models.TextField(blank=False, null=False)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name