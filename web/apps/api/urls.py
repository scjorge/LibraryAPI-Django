from rest_framework import routers
from django.urls import path, include

from apps.api.views.views_sets import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
