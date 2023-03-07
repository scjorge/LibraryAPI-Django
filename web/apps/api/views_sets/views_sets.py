from rest_framework.viewsets import ModelViewSet

from apps.api.models import Category, Publisher, Author, Book, Purchase
from .serializer import (
    CategorySerializer,
    PublisherSerializer,
    AuthorSerializer,
    BookSerializer,
    BookSerializerView,
    PurchaseSerializer
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BoookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BookSerializerView
        return BookSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
