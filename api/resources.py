from tastypie.resources import ModelResource
from api.models import ServiceProvider, ServiceArea
from tastypie.authorization import Authorization


class ServiceProviderResource(ModelResource):
    class Meta:
        queryset = ServiceProvider.objects.all()
        resource_name = 'service_provider'
        authorization = Authorization()

class ServiceAreaResource(ModelResource):
    class Meta:
        queryset = ServiceArea.objects.all()
        resource_name = 'service_area'
        authorization = Authorization()