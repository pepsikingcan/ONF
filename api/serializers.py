'''
Created on 2015-04-30

@author: admin
'''
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
                  'id',
                'description',
                'engine',
                'year',
                'make',
                'owner',
                'photo',
                
                  )