from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('contact/', include('contact.urls'), name='contact'),
    path('', include("newsfeed.urls"), name='newsfeed-urls'),
]
