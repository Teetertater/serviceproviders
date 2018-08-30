## Django REST API using Django REST and postgres (postgis)

CRUD for service providers and their corresponding service areas. 

Please see requirements.txt for prerequisites.

## To start server:
python manage.py runserver

## Query API (Tested with Postman)
To create a provider:   
POST http://localhost:8000/api/service_provider/   
body:

```json
{
	"name": "name",
	"email": "valid@email.com",
	"phone": "+countryphonenumber",
	"language": "en",
	"currency": "USD"
}
```

To retrieve a provider:  
http://localhost:8000/api/service_providers/n     
(optional: n is provider id, e.g 1)


To create a service area for a particular provider:  
POST http://localhost:8000/api/service_areas/  
body:

```json
{
	"name": "sa_name",
	"provider": "name",
	"price": "decimal",
	"area": "POLYGON((0 0, 1 1, 2 2))"
}
```

To view all services areas which contain a particular point:  
http://localhost:8000/api/service_areas_about_point/?point=lat,long     
(latitude and longtitude separated by comma)


