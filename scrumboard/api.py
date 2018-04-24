"""
in this way, django will develop for you the different needed views
to create,update, and delete objects

from rest_framework.viewsets import ModelViewSet
from .serializers import CardSerializer, ListSerializer
from .models import Card, List


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

"""

#This is to implement only the GET method of 'http'
from .serializers import CardSerializer, ListSerializer
from .models import Card, List
from rest_framework.generics import ListAPIView


class ListApi(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer