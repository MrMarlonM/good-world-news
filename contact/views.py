from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your messages was sent successfully.')
            return redirect('home')

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})