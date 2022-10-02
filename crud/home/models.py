from django.db import models

# Create your models here.
class Entry(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    mobile=models.IntegerField()

    def __str__(self):
        return self.name
