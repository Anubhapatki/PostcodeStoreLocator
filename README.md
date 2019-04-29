# PostcodeStoreLocator

This is store locator API implemented using Django REST Framework. Given a postcode and radius it finds all the store locations within that radius

### Prerequisites

Create a virtual environment and activate it

```
python3 -m venv env
```

```
source env/bin/activate
```

### Installing Requirements

Make sure you are in the main directory. Install the requirements.txt using pip install.

```
pip install -r requirements.txt
```
### Create a superuser

You will need a superuser account if you'd want to add new products and edit things in admin.

```
python manage.py createsuperuser
```

### Run the server & login


```
python manage.py runserver
```



## API Access

Go to the following URL.
```
http://127.0.0.1:8000
```
This will list all the stores locations with there latitude and longitude.
```
http://127.0.0.1:8000/stores
```
Generates the list of stores using Django Rest Framework
```
http://127.0.0.1:8000/nearest_locations/<str:postcode>/<int:distance>
```
Queries the database and generates a list of store location within the given distance of the provided postcode


##  Questions to Answer
#### Tell us what test you completed (backend or full-stack)
Backend 

#### If you had more time, what improvements would you make if any?
 I could have looked at authentication of the API which has not been implemented at the moment.
 Also provide better validation of the API and data provided in the URL

#### What bits did you find the toughest? What bit are you most proud of? In both cases, why?
This was my first attempt with Django Rest Framework so took me some time to understand it. Also Postcodes.io nearest locations API just returns a list of postcodes in 20km radius with a limit to 100 so I have used haversine formula to return the distance between the two points
The whole project setup and use of Django Rest Framework is something I am happy about

#### What one thing could we do to improve this test?

More Test scenarios could be added to check the behaviour of the API.
