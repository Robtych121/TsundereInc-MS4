from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    points = models.IntegerField(blank=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
