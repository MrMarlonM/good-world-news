from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'
        ),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/like/', views.article_like, name='article_like'),
    path(
        '<slug:slug>/approve_comment/<int:comment_id>/',
        views.approve_comment, name='approve_comment'
        ),
]