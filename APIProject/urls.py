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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .customopenapi import CustomOpenAPISchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version='v1',
        description="Test description",

    ),
    public=False,
    url="https://api.unolingua.flareon.ru/",
    generator_class=CustomOpenAPISchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('api.urls')),
                  path('', include('makevideo.urls')),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  # path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path('auth/', include('authentication.urls', namespace='authentication')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
