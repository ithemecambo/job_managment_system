from django.urls import path
import random
import secrets
from .views import (
    BlogView,
    BlogDetailView,
    ContactView,
    FAQView,
)


urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blog-details/<slug>'+f"{secrets.token_hex(6)}"+'<int:pk>/', BlogDetailView.as_view(), name='blog-details'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FAQView.as_view(), name='faq'),

]

