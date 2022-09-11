from rest_framework import serializers 
from demo1.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"