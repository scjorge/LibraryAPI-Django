from rest_framework import routers
from django.urls import path, include

from .views_sets import (
    CategoryViewSet,
    PublisherViewSet,
    AuthorViewSet,
    BoookViewSet,
    PurchaseViewSet,
)

router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"publisher", PublisherViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"book", BoookViewSet)
router.register(r"purchase", PurchaseViewSet)


urlpatterns = [
    path("viewset/", include(router.urls)),
]
