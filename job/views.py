from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.list import MultipleObjectMixin
from itertools import chain
from candidate.models import *
from account.models import *


class HomeView(TemplateView):
    template_name = 'user/index.html'


class HomeViewList(ListView):
    template_name = 'user/index.html'
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:8]
        context['companies'] = Company.objects.all()[:4]
        context['job_types'] = JobType.objects.all()
        context['jobs'] = Job.objects.all()[:6]
        context['cities'] = City.objects.all()
        context['candidates'] = Candidate.objects.all()[:12]

        return context


class CategoryView(ListView):
    template_name = 'job/categories.html'
    queryset = SubCategory.objects.all()
    paginate_by = 20


class SubCategoryView(ListView):
    template_name = 'job/categories.html'
    queryset = SubCategory.objects.all().order_by('title')
    paginate_by = 20


class CompanyView(ListView):
    template_name = 'job/companies.html'
    queryset = Company.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Job.objects.all() > 0:
            context['jobs'] = Job.objects.all().order_by('-created_date')
        else:
            context['jobs'] = {}

        return context


class CompanyDetailView(DetailView, MultipleObjectMixin):
    model = Company
    template_name = 'admin/company/company-detail.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        company = Company.objects.get(pk=self.kwargs['pk'])
        object_list = Job.objects.filter(company_id=company)
        context = super(CompanyDetailView, self).get_context_data(object_list=object_list, **kwargs)

        return context


class JobListView(ListView):
    template_name = 'user/job-list.html'
    queryset = Job.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context['job_types'] = JobType.objects.all().order_by('title')
        context['company'] = Company.objects.get(id=1)

        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'user/job-detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        job = Job.objects.get(pk=self.kwargs['pk'])
        context['languages'] = LanguageLevel.objects.all().filter(job=job)
        # context['account'] = Account.objects.get(account=job)
        # context['company'] = Company.objects.get(company=job)

        return context


class SearchView(ListView):
    template_name = 'job/search.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            job_results = Job.objects.search(query)
            company_results = Company.objects.search(query)
            candidate_results = Candidate.objects.search(query)

            queryset_chain = chain(
                job_results,
                company_results,
                candidate_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)
            return qs
        return Job.objects.none()


class SearchResultsView(ListView):
    model = Job
    template_name = 'job/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Job.objects.filter(
            Q(level__icontains=query) | Q(salary__icontains=query)
        )
        return object_list


class LoginView(TemplateView):
    template_name = 'job/login.html'


class RegisterView(TemplateView):
    template_name = 'job/register.html'


class PostJobView(TemplateView):
    template_name = 'job/post-job.html'


class TermPrivacyView(TemplateView):
    template_name = 'job/search.html'
