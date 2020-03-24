from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from accounts.views import FieldsListView

urlpatterns = [
    path(
        'login/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'field_list/',
        FieldsListView.as_view(),
        name='fields_list'
    ),
]
