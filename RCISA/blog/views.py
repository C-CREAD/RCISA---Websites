from django.shortcuts import render
from rest_framework import generics, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost
from .serializers import BlogPostSerializer
from accounts.permissions import IsAdminOrReverend, ReadOnly


class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class BlogPostListCreateView(generics.ListCreateAPIView):
    """
    Display all Blog Posts and allow creation of new posts.
    """
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    pagination_class = BlogPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'content', 'author__full_name']
    filterset_fields = ['author__status', 'author__congregation']
    ordering_fields = ['created_at', 'title']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsAdminOrReverend()]
        return [ReadOnly()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Display selected blog post in detail
    """
    lookup_field = 'slug'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsAdminOrReverend()]
        return [ReadOnly()]


class BlogPostLikeView(APIView):
    """
    Enable like counter for each blog post
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        try:
            post = BlogPost.objects.get(slug=slug)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                return Response({'liked': False, 'count': post.likes.count()}, status=status.HTTP_200_OK)
            else:
                post.likes.add(request.user)
                return Response({'liked': True, 'count': post.likes.count()}, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({'detail': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


class BlogPostShareView(APIView):
    """
    Enable share counter for each blog post
    """
    def post(self, request, slug):
        try:
            post = BlogPost.objects.get(slug=slug)
            post.share_count += 1
            post.save()
            return Response({'shared': True, 'count': post.share_count}, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({'detail': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)