from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserPageSerializer, UserInfoChangeSerializer

# Create your views here.

@api_view(['GET', 'PUT'])
def mypage(request, username):
    if request.user.username != username:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if request.user.username == username:
            user = get_object_or_404(get_user_model(), username=username)
            serializer = UserPageSerializer(user)
            return Response(serializer.data)
        
    elif request.method == 'PUT':
        if request.user.username == username:
            user = get_object_or_404(get_user_model(), username=username)
            serializer = UserInfoChangeSerializer(instance=user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
