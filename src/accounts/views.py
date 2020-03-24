from rest_framework.generics import ListAPIView

from accounts.models import Field, City
from accounts.serializers import FieldSerializer, CitySerializer


class FieldsListView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
