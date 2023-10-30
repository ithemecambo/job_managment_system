from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

from .views import (
    JobViewSet,
)


app_name = 'job'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', obtain_auth_token, name=None),
    path('register/', obtain_auth_token, name=None),

    path('jobs/', JobViewSet.as_view(), name=None),


]