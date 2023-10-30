from django.urls import path
from .views import (
    BlogViewSet,
)

app_name = 'setting'

urlpatterns = [
    path('blogs/', BlogViewSet.as_view(), name=None),
]