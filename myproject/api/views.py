from django.shortcuts import render

from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore


@api_view(['GET'])
def getData(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return Response(data)#This always return the data into JSON format.



