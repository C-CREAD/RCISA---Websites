from django.shortcuts import render
from rest_framework import generics, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sermon
from .serializers import SermonSerializer
from accounts.permissions import IsAdminOrReverend, ReadOnly

class IsAdminOrReverend(permissions.BasePermission):
    """
    Ensures only Admins and Reverend users can create/update/delete sermons
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status in ['admin', 'reverent']

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.status in ['admin', 'reverent']

class SermonListCreateView(generics.ListCreateAPIView):
    """
    Display all Sermon posts and enable creating new ones.
    """
    queryset = Sermon.objects.all().order_by('-date_preached')
    serializer_class = SermonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['preacher__congregation', 'preacher__status', 'date_preached']
    search_fields = ['title', 'description', 'preacher__full_name']
    ordering_fields = ['date_preached', 'created_at']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsAdminOrReverend()]
        return [ReadOnly()]

    def perform_create(self, serializer):
        if not IsAdminOrReverend().has_permission(self.request, self):
            raise permissions.PermissionDenied("Only admins or reverends can create sermons.")
        serializer.save(preacher=self.request.user)


class SermonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Display selected sermon in detail
    """
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsAdminOrReverend()]
        return [ReadOnly()]


class SermonLikeToggle(APIView):
    """
    Increment like counter per selected sermon post
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        sermon = get_object_or_404(Sermon, slug=slug)
        user = request.user
        if user in sermon.likes.all():
            sermon.likes.remove(user)
            liked = False
        else:
            sermon.likes.add(user)
            liked = True
        return Response({'liked': liked, 'count': sermon.likes.count()})


class SermonShare(APIView):
    """
    Increment share counter per selected sermon post
    """
    def post(self, request, slug):
        sermon = get_object_or_404(Sermon, slug=slug)
        sermon.share_count += 1
        sermon.save()
        return Response({'shared': True, 'count': sermon.share_count})


