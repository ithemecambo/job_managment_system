from django.urls import path

from .views import (
    SlideListView,
    NotificationListView,
    CompanySettingView,
    AccountProfileSettingView,
)


urlpatterns = [
    path('banners', SlideListView.as_view(), name='banners'),
    path('notifications', NotificationListView.as_view(), name='notifications'),
    path('company-setting', CompanySettingView.as_view(), name='company-setting'),
    path('account-profile-setting', AccountProfileSettingView.as_view(), name='account-profile-setting'),
]

