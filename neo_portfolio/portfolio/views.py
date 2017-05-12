from django.template import RequestContext
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger    
from portfolio.models import Project, Technology, ProjectImage

# Create your views here.
class IndexView(View):
    """
    """
    def get(self, request):
        projects = Project.objects.all()
        tech_list = Technology.objects.all()
        paginator = Paginator(projects, 10)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        data = {'projects': projects, 'tech_list': tech_list}
        return render(request, 'pages/index.html', data)

class ProjectDetailsView(View):
    """
    """
    def get(self, request, pid):

        project = get_object_or_404(Project, **{'id': pid})
        return render(request, "pages/project_details.html", {'project': project})