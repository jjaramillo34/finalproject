from django.views.generic.edit import CreateView


class ContactView(CreateView):
    template_name = "contact/contact.html"