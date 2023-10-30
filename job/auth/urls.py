from django.urls import path

from .views import (
    DashboardView,
    CategoryListView,
    SubCategoryView,

    CompanyListView,
    JobView,
    JobListView,
    ReportCompanyView,
    ReportUploadJobView,
    ReportApplyJobView,

    add_subcategory,
    TodoListView,
    add_todo,
    delete_todo,
    DeleteTodo,
)


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('add-subcategory', SubCategoryView.as_view(), name='add-subcategory'),

    path('companies', CompanyListView.as_view(), name='companies'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('post-job', JobView.as_view(), name='add-job'),
    path('report-companies', ReportCompanyView.as_view(), name='report-companies'),
    path('report-upload-jobs', ReportUploadJobView.as_view(), name='report-upload-jobs'),
    path('report-apply-jobs', ReportApplyJobView.as_view(), name='report-apply-jobs'),

    path('add-subcategory', add_subcategory, name='add-subcategory'),
    path('todo-list', TodoListView.as_view(), name='todo-list'),
    path('add-todo', add_todo, name='add-todo'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete'),
]

