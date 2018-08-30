from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import ServiceArea, ServiceProvider


class ServiceProviderSerializer(ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ('id', 'name', 'email', 'phone', 'language', 'currency')


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ServiceProviderSerializer(read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = "area"
        fields = ('id', 'name', 'provider', 'price')