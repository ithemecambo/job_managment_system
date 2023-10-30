from django.urls import path
from .views import (
    AccountViewSet,
)

app_name = 'account'

urlpatterns = [
    path('accounts/', AccountViewSet.as_view(), name=None),
    path('account/<int:pk>/', AccountViewSet.as_view(), name=None),
]
