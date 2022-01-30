from app.models import (
    LoginsModel, CidModel, UrlsModel
)
from rest_framework import serializers


class LoginsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginsModel
        fields = '__all__'


class CidSerializer(serializers.ModelSerializer):

    class Meta:
        model = CidModel
        fields = '__all__'


class UrlsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlsModel
        fields = '__all__'
