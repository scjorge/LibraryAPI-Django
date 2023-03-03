from rest_framework.viewsets import ModelViewSet

from apps.api.models import Category
from apps.api.serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
