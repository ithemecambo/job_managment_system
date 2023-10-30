from django.urls import path
from .views import (
    CandidateViewSet,
)

app_name = 'candidate'

urlpatterns = [
    path('candidates/', CandidateViewSet.as_view(), name=None),
    path('candidate/<int:pk>', CandidateViewSet.as_view(), name=None),
]
