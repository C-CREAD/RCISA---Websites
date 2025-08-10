from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, BlogPostLikeView, BlogPostShareView

urlpatterns = [
    path('', BlogPostListCreateView.as_view(), name='blog-list-create'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('<slug:slug>/like/', BlogPostLikeView.as_view(), name='blog-like'),
    path('<slug:slug>/share/', BlogPostShareView.as_view(), name='blog-share'),
]
