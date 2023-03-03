from rest_framework.viewsets import ModelViewSet

from apps.api.models import Category, Publisher
from .serializer import CategorySerializer, PublisherSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer