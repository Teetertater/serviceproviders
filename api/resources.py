from django.contrib.gis.geos import fromstr
from rest_framework import viewsets, exceptions

from .models import ServiceProvider, ServiceArea
from .serializers import ServiceProviderSerializer, ServiceAreaSerializer


class ServiceProviderResource(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

		
class ServiceAreaResource(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

class ServiceAreasOnPoint(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        try:
            #parameter is read as comma-separated coordinate. Use fromstr to try to parse it as a point
            #this will throw an error if anything other than a point is given or format is invalid
            unparsed_point = self.request.GET.get('point', '').replace(',', ' ')
            point = fromstr('POINT({})'.format(unparsed_point))
            return ServiceArea.objects.all().filter(area__contains=point)

        except:
            raise exceptions.ValidationError('invalid point')

        
