"""APIProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .customopenapi import CustomOpenAPISchemaGenerator

schema_view = get_schema_view(
   openapi.Info(
      title="Project API",
      default_version='v1',
      description="Test description",

   ),
   public=True,
   url="http://188.120.235.15:8000",
   generator_class=CustomOpenAPISchemaGenerator,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include('makevideo.urls')),
    path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

