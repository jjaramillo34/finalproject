from django.shortcuts import render
from django.views.generic.edit import CreateView
from contact.forms import ContactForm
    
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