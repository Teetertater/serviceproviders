"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url, include
from django.contrib import admin
from api.resources import ServiceProviderResource, ServiceAreaResource

service_provider = ServiceProviderResource()
service_area = ServiceAreaResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(service_provider.urls)),
    url(r'^api/', include(service_area.urls)),
]
