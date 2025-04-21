from django.shortcuts import render

from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from base.models import Item # type: ignore
from .serializers import ItemSerializer # type: ignore


@api_view(['GET'])
def getData(request):
    items = Item.objects.all() #This will get all the data from the database.
    serializer= ItemSerializer(items, many=True)
    return Response(serializer.data)#This always return the data into JSON format.



