from email import header
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic

from about.models import About, Members

class AboutViewDetail(generic.DetailView):
    model = About
    template_name = "about/about.html"
    
def about(request):
    context_dict = {}
    header = "About Us"
    subheader = "This is what we do"
    teams = About.objects.all()
    members = Members.objects.all()
    context_dict = {'header':header, 'subheader':subheader, 'teams':teams, 'members':members}
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="about/about.html"
    )