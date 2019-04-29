
import requests, json
import unittest

# Create your tests here.


class TestNearByPostCodes(unittest.TestCase):

    def test_access_stores_api(self):
        resp = requests.get('http://127.0.0.1:8000/stores')
        print (resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_near_by_postcodes(self):
        postcode = 'RG20GY'
        distance = 10
        nearest_stores = ['RG30 1PR', "RG41 5HH", 'RG2 0HB', 'RG40 2NU' ]

        resp = requests.get('http://127.0.0.1:8000/nearest_locations/{}/{}'.format(postcode,distance))
        nearest_stores_returned = [location["postcode"] for location in resp.json()]
        self.assertEqual(nearest_stores,nearest_stores_returned)

    def test_valid_request(self):
        resp = requests.get('http://127.0.0.1:8000/nearest_locations/')
        self.assertEqual(resp.status_code, 404)
        pass






if __name__ == '__main__':
    unittest.main()