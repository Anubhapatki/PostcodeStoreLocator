from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from stores.models import Stores
import requests

import json
from operator import itemgetter

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


