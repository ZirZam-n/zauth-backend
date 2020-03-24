from rest_framework.generics import ListAPIView

from accounts.models import Field, City, University
from accounts.serializers import FieldSerializer, CitySerializer, UniversitySerializer


class FieldsListView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UniversityListView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
