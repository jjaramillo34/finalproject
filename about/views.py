from django.views.generic.edit import CreateView


class AboutView(CreateView):
    template_name = "about/about.html"
    
    