from django.shortcuts import render
from .serializers import PortSerializer,ExperienceSerializer
from rest_framework import viewsets
from rest_framework import mixins
from .models import Projectmodel,ExperienceModel


# Create 
# your views here.

class Portfolioview(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class = PortSerializer
    queryset = Projectmodel.objects.all()

class Expview(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class = ExperienceSerializer
    queryset = ExperienceModel.objects.all()