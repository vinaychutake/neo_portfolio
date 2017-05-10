from django.template import RequestContext
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404

from portfolio.models import Project, Technology, ProjectImage

# Create your views here.
class IndexView(View):
    """
    """
    def get(self, request):
        projects = Project.objects.filter(is_active=True)
        tech_list = Technology.objects.all()
        data = {'projects': projects, 'tech_list': tech_list}
        return render(request, 'pages/index.html', data)

class ProjectDetailsView(View):
    """
    """

    def get(self, request, pid):

        project = get_object_or_404(Project, **{'id': pid})
        return render(request, "pages/project_details.html", {'project': project})