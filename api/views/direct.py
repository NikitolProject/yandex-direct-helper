from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from app.models import (
    LoginsModel, CidModel, UrlsModel
)
from api.serializers.direct import (
    LoginsSerializer, CidSerializer, UrlsSerializer
)


@extend_schema(description='Logins')
class LoginsView(ModelViewSet):
    """
    Logins endpoint
    """
    serializer_class = LoginsSerializer
    queryset = LoginsModel.objects.all()


@extend_schema(description='Cid')
class CidView(ModelViewSet):
    """
    Cid endpoint
    """
    serializer_class = CidSerializer
    queryset = CidModel.objects.all()


@extend_schema(description='Urls')
class UrlsView(ModelViewSet):
    """
    Urls endpoint
    """
    serializer_class = UrlsSerializer
    queryset = UrlsModel.objects.all()
