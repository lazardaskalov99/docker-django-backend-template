from django.urls import path, include

from apps.gateway.ping import ping

urlpatterns = [
    path('web/ping/', ping),
]
