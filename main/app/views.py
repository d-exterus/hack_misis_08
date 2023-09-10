from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import UserAuth, User, Team
from .serializers import UserSerializer, TeamSerializer


# Create your views here.

@api_view(['POST'])
def user_create(request: Request):
    user = UserSerializer(data=request.data)
    if user.is_valid(raise_exception=True) and ('login' in request.data) and ('hash' in request.data):
        user.save()
        user_auth = UserAuth(login=request.data['login'], hash=request.data['hash'])
        user_auth.user_id = user.instance.id
        user_auth.save()
    return Response(data={'id': user.instance.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_get(request: Request, id: int):
    try:
        user = User.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(data=UserSerializer(instance=user).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def team_create(request: Request):
    team = TeamSerializer(data=request.data)
    if team.is_valid(raise_exception=True):
        team.save()
    return Response(data={'id': team.instance.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def team_get(request: Request, id: int):
    try:
        team = Team.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(data=UserSerializer(instance=team).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def leaderboard(request: Request):
    if request.query_params['type'] == 'TEAM':
        cls = Team
        serializer = TeamSerializer
    elif request.query_params['type'] == 'USER':
        cls = User
        serializer = UserSerializer
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    objs = cls.objects.order_by('-count')[:10]
    return Response(data=serializer(objs, many=True).data, status=status.HTTP_200_OK)
