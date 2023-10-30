from django.views.generic import ListView, DetailView, TemplateView
from setting.models import *


class SlideListView(ListView):
    template_name = 'admin/banner/banners.html'
    queryset = Slider.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(SlideListView, self).get_context_data(**kwargs)

        return context


class NotificationListView(ListView):
    template_name = 'admin/notification/notifications.html'
    queryset = Notification.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)

        return context


class AccountProfileSettingView(TemplateView):
    template_name = 'admin/setting/account-profile-setting.html'


class CompanySettingView(TemplateView):
    template_name = 'admin/setting/company-setting.html'



