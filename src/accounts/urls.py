from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from accounts.views import FieldsListView, CityListView, UniversityListView, RegisterUserView


def temp_view(*args, **kwargs):
    pass


urlpatterns = [
    path(
        'login/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'register/',
        RegisterUserView.as_view(),
        name='register',
    ),
    path(
        'verify/',
        temp_view,
        name='verify_email',
    ),
    path(
        'change_password/',
        temp_view,
        name='change_password',
    ),
    path(
        'edu/',
        temp_view,
        name='edu_info',
    ),
    path(
        'profile',
        temp_view,
        name='profile',
    ),
    path(
        'refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path(
        'field_list/',
        FieldsListView.as_view(),
        name='field_list',
    ),
    path(
        'city_list/',
        CityListView.as_view(),
        name='city_list',
    ),
    path(
        'university_list/',
        UniversityListView.as_view(),
        name='university_list',
    ),
]
