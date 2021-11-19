from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='Blog'),
    path('posts/<str:category_name>/', views.post_list, name='post-list'),
    path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/detail/<int:post_id>/<str:message>/', views.post_detail, name='post-detail-message'),

]