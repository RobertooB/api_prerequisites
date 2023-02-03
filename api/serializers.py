from rest_framework import serializers
from api.models import  Prerequisites, PrerequisitesForm

class PrerequisitesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Prerequisites
        fields = "__all__"

class PrerequisitesFormSerializer (serializers.ModelSerializer):
    class Meta:
        model = PrerequisitesForm
        fields = "__all__"