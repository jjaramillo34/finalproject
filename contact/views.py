from django.shortcuts import render
from django.views import generic
from contact.forms import ContactForm
from django.contrib import messages

class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    
    def get_success_url(self) -> str:
        return self.request.path
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'You Message Has Been Send Successfully')
        return super().form_valid()
    
    def form_invalid(self, form):
        form.add_error(None, 'Oops... something went wrong with the form')
        return super().form_invalid(form)
    
def contact_view(request):
    header = "Contact Us"
    subheader = "Send us an Email"
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'header':header, 'subheader':subheader, 'form': form}
    return render(request, 'contact/contact.html', context)