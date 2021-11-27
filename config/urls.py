from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #drf auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # for authentication
    # path('auth/', include('dj_rest_auth.urls')), # for authentication (you can update url fyi)
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # for reg (depends on allauth)
    # path('accounts/', include('allauth.urls')), #for registration (dj-rest-auth dependency)
]
