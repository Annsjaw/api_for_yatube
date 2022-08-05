from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
