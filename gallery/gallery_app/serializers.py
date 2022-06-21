from rest_framework import serializers
from .models import imageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=imageModel
        fields='__all__'
