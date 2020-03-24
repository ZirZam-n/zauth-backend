from rest_framework.generics import ListAPIView

from accounts.models import Field
from accounts.serializers import FieldSerializer


class FieldsListView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
