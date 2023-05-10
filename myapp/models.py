from django.db import models

class pro(models.Model):
    name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    create = models.DateTimeField ()
    expir = models.DateTimeField()