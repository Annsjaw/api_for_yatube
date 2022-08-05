from posts.models import Group, Post
from rest_framework import viewsets

from .permissions import AuthorOrReadOnly, ReadOnly

from.serializers import (PostSerializer, GroupSerializer)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly, )
