from django.urls import path
from .views import BlogPostCreateView, BlogPostUpdateView, BlogPostListView

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('update/<int:id>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('all/', BlogPostListView.as_view(), name='blogpost_list'),
]