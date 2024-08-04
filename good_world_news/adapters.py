from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    A custom adapter for django-allauth to handle login redirects.

    Overrides the `get_login_redirect_url` method to redirect users based on their role:
    - Staff members and superusers are redirected to the Django admin panel.
    - All other users (regular visitors and moderators) are redirected to the homepage.
    """
    def get_login_redirect_url(self, request):
        """
        Determines the URL to redirect to after a successful login.

        Args:
            request: The current HTTP request object.

        Returns:
            str: The URL to redirect to.
        """
        if request.user.is_staff or request.user.is_superuser:
            return reverse('admin:index')
        else:
            return reverse('home')