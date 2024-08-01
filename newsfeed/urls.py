from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]