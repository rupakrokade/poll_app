from django.conf.urls import url, include

from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=
        Project.objects.all().order_by("-date")[:25],
        template_name="project/project.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model = Post, template_name = "project/project.html"))
]
