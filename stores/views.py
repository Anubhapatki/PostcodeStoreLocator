from django.shortcuts import render
from .models import Stores
from rest_framework.views import  APIView
from .serializers import StoresSerializer
from rest_framework.response import Response
from django.db.models import Q
import math
import requests
from haversine import haversine

import json
from operator import itemgetter

class StoreLocation(APIView):

    def get(self,request, format=None):


        stores=Stores.objects.all().order_by('location')
        serializer = StoresSerializer(stores, many=True)
        return Response(serializer.data)

class NearestStoresToLocation(APIView):


    def get(self,request,postcode, distance):

        nearest_locations=getPostCodesInRadius(postcode,distance)
        serializer = StoresSerializer(nearest_locations, many=True)
        return  Response(serializer.data)


def index(request):

    Stores.objects.all().delete()
    with open('stores.json') as f:
        data = json.load(f)
    for d in data:
        store = Stores(
            location = d['name'],
            postcode = d['postcode']
            )
        store.save()

    data.sort(key=itemgetter('name'))
    data_log_lat = getPostCodesLatitudeLogitude(data)

    for data in data_log_lat["result"]:
        try:
            store = Stores.objects.filter(postcode = data["query"]).\
                update(longitude = data["result"]["longitude"],
                       latitude=data["result"]["latitude"])
            store.save()
        except:
            pass

    context = {'Stores': Stores.objects.all().order_by('location')}
    return render(request, 'stores/index.html', context)



def getPostCodesLatitudeLogitude(data):
    postcode_data = { "postcodes": [ d['postcode'] for d in data ]}
    headers = {'Content-Type': 'application/json'}
    resp = requests.post('https://api.postcodes.io/postcodes/', data=json.dumps(postcode_data), headers=headers)
    resp.json()
    return json.loads(resp.text)


def getPostCodesInRadius(postcode, distance):
    #Find longitude and latitude of a given postcode
    response = requests.get('https://api.postcodes.io/postcodes/{}'.format(postcode))
    response_json = json.loads(response.text)


    postcode_latitude = response_json["result"]["latitude"]
    postcode_longitude = response_json["result"]["longitude"]


    if postcode_latitude and postcode_longitude:
        lat = float(postcode_latitude)
        lon = float(postcode_longitude)

        """
        # Haversine formula = https://en.wikipedia.org/wiki/Haversine_formula
        R = 6378.1  # earth radius
        bearing = 1.57  # 90 degrees bearing converted to radians.
        distance = int(distance)

        lat1 = math.radians(lat)  # lat in radians
        long1 = math.radians(lon)  # long         in radians
        print(lat1, long1)

        lat2 = math.asin(math.sin(lat1) * math.cos(distance / R) +
                         math.cos(lat1) * math.sin(distance / R) * math.cos(bearing))

        long2 = long1 + math.atan2(math.sin(bearing) * math.sin(distance / R) * math.cos(lat1),
                                   math.cos(distance / R) - math.sin(lat1) * math.sin(lat2))

        lat2 = round(math.degrees(lat2), 5)
        long2 = round(math.degrees(long2), 5)

        print(lat2, long2)

        


        queryset = Stores.objects.filter(latitude__gte=lat1, latitude__lte=lat2) \
            .filter(longitude__gte=long1, longitude__lte=long2)
        """
        #queryset = Stores.objects.filter(
         #   Q(latitude__range = (lat2, round(lat,5)))
           #& Q(longitude__range=(long2, round(lon,5)))
        #)
        locations=list()
        queryset = Stores.objects.all().order_by('-latitude')
        for store in queryset:
            lat2=store.latitude
            long2=store.longitude

            if long2 and lat2:

                radius = haversine((lat,lon),(lat2,long2))
                if radius <= distance:
                    locations.append(store)

        print (queryset.query)

        print ([q.location for q in queryset])

    return locations


