from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, TemplateView, DeleteView, CreateView
from candidate.models import *
from job.forms import *
from job.models import *


class DashboardView(ListView):
    template_name = 'admin/dashboard/dashboard.html'
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['candidates'] = Candidate.objects.filter(status=True).order_by('-created_date')[:5]

        return context


class HomeView(ListView):
    template_name = 'admin/dashboard/dashboard.html'
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['candidates'] = Candidate.objects.all().order_by('-created_date')[:5]

        return context


class CategoryListView(ListView):
    template_name = 'admin/category/categories.html'
    queryset = SubCategory.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryCreateForm
    success_url = reverse_lazy('../categories')
    template_name = 'admin/category/add-subcategory.html'


class SubCategoryView(View):

    def render(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'admin/category/add-subcategory.html', context)

    def post(self, request):
        self.form = SubCategoryCreateForm(request.POST, request.FILES)
        if self.form.is_valid():
            self.form.save()
            return redirect('../categories')
        return self.render(request)

    def get(self, request):
        self.form = SubCategoryCreateForm()
        return self.render(request)


def add_subcategory(request):
    form = SubCategoryCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Category Saved Success')
        return redirect('../categories')
    context = {
        'title': 'Add Category',
        'form': form
    }
    return render(request, 'admin/category/add-category.html', context)


def update_subcategory(request, pk):
    queryset = SubCategory.objects.get(id=pk)
    form = SubCategoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = SubCategoryUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Updated Success')
            return redirect('../categories')
    context = {
        'title': 'Update Category',
        'form': form
    }
    return render(request, 'admin/category/add-category.html', context)


def delete_subcategory(request, pk):
    queryset = SubCategory.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Category Deleted Success')
    return redirect('../categories')


class TodoListView(ListView):
    template_name = 'admin/todo/todo-list.html'
    queryset = Todo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)

        return context


def add_todo(request):
    form = TodoCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/auth/todo-list')
    context = {
        'title': 'Add Todo',
        'form': form
    }
    return render(request, 'admin/todo/add-todo.html', context)


def delete_todo(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()
    return redirect('/auth/todo-list')


class DeleteTodo(DeleteView):
    model = Todo
    success_url = '/auth/todo-list'


class CompanyView(TemplateView):
    template_name = 'admin/company/companies.html'


class CompanyListView(ListView):
    template_name = 'admin/company/companies.html'
    queryset = Company.objects.all().order_by('-id')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)

        return context


class JobView(TemplateView):
    template_name = 'admin/job/add-job.html'

    # def post(self, request, *args, **kwargs):
    #     form = JobCreateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         text = form.cleaned_data('data')
    #         form = JobCreateForm()
    #         redirect('jobs')
    #
    #     args = {'form': form, 'text': text}
    #     return render(request, self.template_name, args)

    def post(self, request):
        self.form = JobCreateForm(request.POST, request.FILES)
        if self.form.is_valid():
            self.form.save()
            return redirect('../jobs')
        return self.render(request)


class JobListView(ListView):
    template_name = 'admin/job/jobs.html'
    queryset = Job.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ReportCompanyView(ListView):
    template_name = 'admin/report/report-companies.html'
    queryset = Company.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ReportCompanyView, self).get_context_data()

        return context


class ReportUploadJobView(ListView):
    template_name = 'admin/report/report-upload-jobs.html'
    queryset = Job.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ReportUploadJobView, self).get_context_data()

        return context


class ReportApplyJobView(ListView):
    template_name = 'admin/report/report-apply-jobs.html'
    queryset = Job.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ReportApplyJobView, self).get_context_data()

        return context


