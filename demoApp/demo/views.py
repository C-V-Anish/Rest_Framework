from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from demo1.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def GetData(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
