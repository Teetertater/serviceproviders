## Django REST API using tastypie and postgres (postgis)

CRUD for service providers and their corresponding service areas. 

Prerequisites:
* Python 2.7
* Postgres with postgis 2.4
* Django 2.0+
* django-phonenumber-field
* django-money
* django-language-field

## To start server:
python manage.py runserver

## Query API (Tested with Postman)
To create a provider: 
POST http://localhost:8000/api/service_provider/ 
body:
{
	"name": "name",
	"email": "valid@email.com",
	"phone": "+countryphonenumber",
	"language": "en",
	"currency": "USD"
}

To retrieve a provider:
http://localhost:8000/api/service_provider/n    (n is provider id, e.g 1)

To create a service area for a particular provider:
POST http://localhost:8000/api/service_area/
body:
{
	"name": "sa_name",
	"provider": "name",
	"price": "decimal",
	"area": "POLYGON((0 0, 1 1, 2 2))"
}

