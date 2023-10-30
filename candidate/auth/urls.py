from django.urls import path

from .views import (
    CandidateListView,
    ReportCandidateView,
)

urlpatterns = [
    path('candidates', CandidateListView.as_view(), name='candidates'),
    path('report-candidates', ReportCandidateView.as_view(), name='report-candidates'),
]

