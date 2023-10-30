from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import render, redirect
from candidate.forms import *
from candidate.models import *


class CandidateView(TemplateView):
    template_name = 'admin/candidate/candidates.html'


class CandidateListView(ListView):
    template_name = 'admin/candidate/candidates.html'
    queryset = Candidate.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CandidateCreateView(View):
    def render(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'admin/candidate/add-candidate.html', context)

    def post(self, request):
        self.form = CandidateCreateForm(request.POST, request.FILES)
        if self.form.is_valid():
            self.form.save()
            return redirect('../candidates')
        return self.render(request)

    def get(self, request):
        self.form = CandidateCreateForm()
        return self.render(request)


class CandidateDetailView(DetailView):
    model = Job
    template_name = 'admin/candidate/candidate-detail.html'

    def get_context_data(self, **kwargs):
        context = super(CandidateDetailView, self).get_context_data(**kwargs)
        job = Job.objects.get(pk=self.kwargs['pk'])
        context['languages'] = LanguageLevel.objects.all().filter(job=job)

        return context


class ReportCandidateView(ListView):
    template_name = 'admin/report/report-candidates.html'
    queryset = Candidate.objects.all().order_by('-created_date')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

