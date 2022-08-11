from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LocationAPIVIew(APIView):
    def get(self, request):
        if 'lag' not in request.GET:
            return Response("bad", status=status.HTTP_400_BAD_REQUEST)
        if 'lon' not in request.GET:
            return Response("bad", status=status.HTTP_400_BAD_REQUEST)

        return Response("good", status=status.HTTP_200_OK)
