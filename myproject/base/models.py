from django.db import models #type: ignore

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
