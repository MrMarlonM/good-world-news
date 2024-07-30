from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        
        if request.user.is_staff or request.user.is_superuser:
            return reverse('admin:index')
        else:
            return reverse('home')