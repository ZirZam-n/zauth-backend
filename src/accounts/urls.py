from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from accounts.views import FieldsListView, CityListView, UniversityListView, RegisterUserView

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
        None,
        name='verify_email',
    ),
    path(
        'change_password/',
        None,
        name='change_password',
    ),
    path(
        'edu/',
        None,
        name='edu_info',
    ),
    path(
        'profile',
        None,
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
