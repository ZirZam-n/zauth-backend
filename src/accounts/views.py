from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response

from accounts.messages import REGISTER_SUCCESS_MESSAGE
from accounts.models import Field, City, University, ZUser
from accounts.serializers import FieldSerializer, CitySerializer, UniversitySerializer, UserRegisterSerializer


class RegisterUserView(GenericAPIView):
    queryset = ZUser.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.create(data=serializer.validated_data)
                user.setup_verification_token()
                user.send_activation_email()
                return Response(
                    {
                        'detail': REGISTER_SUCCESS_MESSAGE,
                    },
                    status=200
                )
            except Exception as e:
                print(e)
                return Response(
                    {'error': 'Could not create user or send mail'},
                    status=406
                )
        else:
            return Response(
                {'error': 'Error occurred during User creation'},
                status=500
            )


class FieldsListView(ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UniversityListView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
