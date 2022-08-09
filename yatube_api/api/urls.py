from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
v1_router.register(r'follow', FollowViewSet)

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt_veryfy'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/', include(jwt_patterns)),
]
