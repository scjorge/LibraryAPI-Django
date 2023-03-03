from rest_framework import routers
from django.urls import path, include

from .views_sets import CategoryViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'publisher', PublisherViewSet)


urlpatterns = [
    path('viewset/', include(router.urls)),
]
