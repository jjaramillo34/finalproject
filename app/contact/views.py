from django.shortcuts import render
from django.core.mail import send_mail
from django.views import generic
from contact.forms import ContactForm
from django.contrib import messages
from django.conf import settings

class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = 'Contact Us'
        context["subheader"] = 'Send us an Message'
        return context
    
    def get_success_url(self) -> str:
        return self.request.path
    
    def form_valid(self, form):
        form.save()
        email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
        email_message = form.cleaned_data['message']
        #send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
        send_mail(
            email_subject,
            email_message,
            'contactme@datanaly.st',
            ['contact@datanaly.st'],
            fail_silently=False,
        )
        messages.add_message(self.request, messages.INFO, 'You Message Has Been Send Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, 'Oops... something went wrong with the form')
        return super().form_invalid(form)
    
def contact_view(request):
    header = "Contact Us"
    subheader = "Send us an Email"
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
        email_message = form.cleaned_data['message']
        send_mail(
            email_subject,
            email_message,
            'contactme@datanaly.st',
            ['contact@datanaly.st'],
            fail_silently=False,
        )
        #send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
        return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'header':header, 'subheader':subheader, 'form': form}
    return render(request, 'contact/contact.html', context)
    
    