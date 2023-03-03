from rest_framework.serializers import ModelSerializer

from apps.api.models import Category, Publisher, Author


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