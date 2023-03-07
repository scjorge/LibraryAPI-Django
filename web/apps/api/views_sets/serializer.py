from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from apps.api.models import Category, Publisher, Author, Book, Purchase, ItemPurchase


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
    class Authorview(ModelSerializer):
        class Meta:
            model = Author
            fields = ["name"]

    author = Authorview(many=True)

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1


class ItemPurchaseSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItemPurchase
        fields = [
            "book",
            "amount",
            "total",
        ]
        depth = 2

    def get_total(self, instance):
        return instance.amount * instance.book.amount


class PurchaseSerializer(ModelSerializer):
    user = CharField(source="user.email")
    status = SerializerMethodField()
    itens = ItemPurchaseSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ["id", "user", "status", "itens", "total"]

    def get_status(self, instance):
        return instance.get_status_display()
