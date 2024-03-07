from .models import Projectmodel,ExperienceModel
from rest_framework import serializers

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectmodel
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = "__all__"
