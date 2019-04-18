from django.db import models

class PostCode(models.Model):
    postcode = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

