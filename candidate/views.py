from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class CandidateView(ListView):
    template_name = 'job/candidate.html'
    queryset = Candidate.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'job/candidate-details.html'

    def get_context_data(self, **kwargs):
        context = super(CandidateDetailView, self).get_context_data(**kwargs)
        candidate = Candidate.objects.get(pk=self.kwargs['pk'])
        context['experiences'] = Experience.objects.all().filter(candidate=candidate)
        context['educations'] = EducationLevel.objects.all().filter(candidate=candidate)
        # context['responsibilities'] = Responsibility.objects.all().filter(candidate=candidate)
        context['portfolios'] = Portfolio.objects.all().filter(candidate=candidate)

        return context


class ResumeView(TemplateView):
    template_name = 'job/resume.html'

