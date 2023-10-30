from django.urls import path
import secrets
from .views import (
    CandidateView,
    CandidateDetailView,
    ResumeView,
)


urlpatterns = [
    path('candidates/', CandidateView.as_view(), name='candidates'),
    path('candidate-details/<position>'+f"{secrets.token_hex(6)}"+'<int:pk>/',
         CandidateDetailView.as_view(), name='candidate-details'),
    path('resume/', ResumeView.as_view(), name='resume'),
]

