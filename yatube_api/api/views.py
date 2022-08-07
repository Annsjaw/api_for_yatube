from django.shortcuts import get_list_or_404, get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import viewsets

from .permissions import AuthorOrReadOnly, GetOrPostAuthOnly, ReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_list_or_404(Post, id=post_id)
        print(post)
        serializer.save(author=self.request.user, post=post[0])


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (GetOrPostAuthOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        following = get_list_or_404(Follow, user=self.request.user)
        return following
