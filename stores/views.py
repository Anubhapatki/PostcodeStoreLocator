from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

import json
from operator import itemgetter

def index(request):
    with open('stores.json') as f:
        data = json.load(f)
    data.sort(key=itemgetter('name'))
    data_log_lat = getPostCodesLatitudeLogitude(data)

    postcodes_log_lat =list()

    for data in data_log_lat["result"]:

        try:
            print("data{}".format(data))
            postcodes_log_lat_dict = dict()



            postcodes_log_lat_dict["postcodes"] = data["query"]
            postcodes_log_lat_dict["location"] = data["result"]["ced"]

            postcodes_log_lat_dict["longitude"] = data["result"]["longitude"]
            postcodes_log_lat_dict["latitude"] = data["result"]["latitude"]
            postcodes_log_lat.append(postcodes_log_lat_dict)
        except:
            pass

    return JsonResponse(postcodes_log_lat, safe=False)
    #return render(request, '/Users/Anubha.Vijay/storelocator/storelocator/templates/stores/index.html', data)
    #return HttpResponse(data)

def postcodes(request):
    with open('../stores.json') as f:
        data = json.load(f)
    data.sort(key=itemgetter('name'))
    return render(request, 'index.html', data)
    #return JsonResponse(data, safe=False)


def getPostCodesLatitudeLogitude(data):
    postcode_data = { "postcodes": [ d['postcode'] for d in data ]}
   # print ("postcode_data:{}".format(json.dumps(postcode_data)))
    headers = {'Content-Type': 'application/json'}

    resp = requests.post('https://api.postcodes.io/postcodes/', data=json.dumps(postcode_data), headers=headers)
   # print(resp.text)
    resp.json()
   # print(resp)
    return json.loads(resp.text)


