from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from .models import UserAuth, User
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
@parser_classes([JSONParser])
def create_auth(request):
    user = User()
    user.save()
    auth = UserAuth(user_id=user.id, **request.data)
    auth.save()
    return JsonResponse({'id': user.id})

@api_view(["POST"])
@parser_classes([JSONParser])
def create_user(request):
    try:
        user = User.objects.get(id = request.data['id'])
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    user.group = request.data['group']
    user.save()
    ser = UserSerializer(user)
    return Response(ser.data)
