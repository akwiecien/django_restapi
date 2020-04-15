from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from data.models import DataContinent, DataCountry, DataCity
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def world(request):
    if request.method == 'GET':
        try:
            # get data from database
            continents = DataContinent.objects.all()
            # serialize
            serializer = ContinentSerializer(continents, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as ex:
            print(f'During "GET" an error accour: {ex}')
            return HttpResponse(status=500)
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            serializer = ContinentSerializer(data=data)

            if serializer.is_valid():
                # serializer.save()
                return JsonResponse(serializer.data, status=201)

        except Exception as ex:
            print(f'During "POST" an error accour: {ex}')
            return HttpResponse(status=500)
         

# Create your views here.
