from rest_framework import routers
from django.urls import path, include

from .views_sets import CategoryViewSet, PublisherViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'author', AuthorViewSet)


urlpatterns = [
    path('viewset/', include(router.urls)),
]
