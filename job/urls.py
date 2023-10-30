from django.urls import path
import secrets
from .views import (
    HomeView,
    SubCategoryView,
    CompanyView,
    CompanyDetailView,
    JobListView,
    JobDetailView,
    SearchView,
    SearchResultsView,
    LoginView,
    RegisterView,
    PostJobView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('categories/', SubCategoryView.as_view(), name='categories'),
    path('companies/', CompanyView.as_view(), name='companies'),
    path('company-detail/<company_industry>'+f"{secrets.token_hex(6)}"+'<int:pk>/',
         CompanyDetailView.as_view(), name='company-details'),
    path('job-lists/', JobListView.as_view(), name='job-lists'),
    path('job-detail/<function>'+f"{secrets.token_hex(6)}"+'<int:pk>/',
         JobDetailView.as_view(), name='job-detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('search-result/', SearchResultsView.as_view(), name='search-result'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('post-job/', PostJobView.as_view(), name='post-job'),


]

