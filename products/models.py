from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length= 40)
    desc = models.TextField(null= True , blank = True)
    price = models.DecimalField(decimal_places=2,max_digits= 10000)
    summary = models.TextField(blank= True, null= True)
    image = models.ImageField(blank = True, null = True , upload_to = 'media')