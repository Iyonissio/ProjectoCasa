from django.db.models import query
from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.serializers import Serializer
from .models import Realtor
from .serializers import RealtorSerializer

class RealtorListView(ListAPIView):
    permissions_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.all()
    Serializer_class = RealtorSerializer
    pagination_class = None

class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, ) 
    queryset = Realtor.objects.filter(mais_vendido=True)
    serializer_class = RealtorSerializer
    pagination_class = None