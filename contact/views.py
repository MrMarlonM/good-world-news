from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_form(request):
    """
    Handles the rendering and submission of the contact form.

    - GET requests: Renders the contact form template with an empty
                    form instance.
    - POST requests: Processes the submitted contact form data.
        - If the form is valid:
            - Saves the form data to the database.
            - Adds a success message to the request.
            - Redirects to the homepage.

    Template:
    - Renders the 'contact/contact.html' template.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your messages was sent successfully.')
            return redirect('home')

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
