from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=32, default="")

    description = models.TextField(max_length=100, default="")
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
