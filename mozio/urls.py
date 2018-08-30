"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from api.resources import ServiceProviderResource, ServiceAreaResource, ServiceAreasOnPoint

router = SimpleRouter()
router.register('service_providers', ServiceProviderResource, 'provider')
router.register('service_areas', ServiceAreaResource, 'service_area')
router.register('service_areas_about_point', ServiceAreasOnPoint, 'return_sa')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
