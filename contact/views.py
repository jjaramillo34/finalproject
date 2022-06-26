from django.shortcuts import render
from django.views.generic.edit import CreateView
from contact.models import Contact

class ContactView(CreateView):
    template_name = "contact/contact.html"
    
def contact(request):
    contact = Contact.objects.all()

    context_dict = {
        'contact': contact
    }

    return render(
        request=request,
        context=context_dict,
        template_name="contact/contact.html"
    )