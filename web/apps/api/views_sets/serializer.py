from rest_framework.serializers import ModelSerializer

from apps.api.models import Category, Publisher, Author, Book


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    
class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializerView(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1