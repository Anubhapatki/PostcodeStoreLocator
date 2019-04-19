from django.db import models

class Stores(models.Model):
    postcode = models.CharField(max_length=7)
    location = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=False, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=False, null=True)


