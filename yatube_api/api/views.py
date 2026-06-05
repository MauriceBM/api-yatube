from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)

from posts.models import Post, Group, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
    )

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(
            post_id=post_id
        ).select_related('author')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        serializer.save(
            author=self.request.user, post_id=post_id
        )
