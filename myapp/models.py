from django.db import models
from rest_framework.serializers import ModelSerializer
class First(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return (f"name -> {self.name} | price -> {self.price}")
    

class FirsSerializer(ModelSerializer):
    class Meta:
        model = First
        fields = ['name', 'price']



