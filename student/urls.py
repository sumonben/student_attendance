from django.contrib import admin
from django.urls import path,include, re_path
from . import views 
from django import views as django_views

urlpatterns = [
    
        path('', views.frontPage, name='frontpage'),
        path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),



]