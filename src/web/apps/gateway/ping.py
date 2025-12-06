from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes([AllowAny])
def ping(request):
    return JsonResponse("pong", safe=False, status=status.HTTP_200_OK)
