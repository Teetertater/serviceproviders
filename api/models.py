# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField, CurrencyField
from languages.fields import LanguageField


#ServiceProvider model
class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    language = LanguageField(default='en')
    currency = CurrencyField(default='USD')

    def __str__(self):
        return self.name

#ServiceArea model. One-to-many relationship with ServiceProvider
class ServiceArea(models.Model):
    provider = models.ForeignKey(ServiceProvider, null=True)
    name = models.CharField(max_length=200)
    price = MoneyField(max_digits=100, decimal_places=4)
    area = models.PolygonField()

    def __str__(self):
        return self.name

