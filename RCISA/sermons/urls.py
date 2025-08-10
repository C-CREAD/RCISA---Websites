from django.urls import path
from .views import SermonListCreateView, SermonDetailView, SermonLikeToggle, SermonShare

urlpatterns = [
    path('', SermonListCreateView.as_view(), name='sermon-list'),
    path('<slug:slug>/', SermonDetailView.as_view(), name='sermon-detail'),
    path('<slug:slug>/like/', SermonLikeToggle.as_view(), name='sermon-like'),
    path('<slug:slug>/share/', SermonShare.as_view(), name='sermon-share'),
]
