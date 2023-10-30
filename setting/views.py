from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class BlogView(ListView):
    template_name = 'job/blog.html'
    queryset = Blog.objects.all()
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'job/blog-details.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog = Blog.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.all().filter(
            blog_id=blog)
        context['count'] = Comment.objects.all().filter(
            blog_id=blog).count()
        return context


class ContactView(TemplateView):
    template_name = 'job/contact.html'


class FAQView(ListView):
    template_name = 'job/faq.html'
    queryset = FAQ.objects.all()

