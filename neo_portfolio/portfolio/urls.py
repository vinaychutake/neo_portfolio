from django.conf.urls import url

from portfolio.views import IndexView, ProjectDetailsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^projects/(?P<pid>[0-9]+)/$', ProjectDetailsView.as_view(), name='project_details'),
]