from django.db import models
from apps.user.models import UserProfile

class  Category(models.Model):
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "tb_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.description[0:15])


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField()

    class Meta:
        db_table = "tb_publisher"
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
    
    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    
    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    amount = models.PositiveIntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    author = models.ManyToManyField(Author, related_name='books')

    class Meta:
        db_table = "tb_book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        return str(self.title)

    
class Purchase(models.Model):
    class StatusPurchase(models.IntegerChoices):
        CART = 1, 'On Cart'
        MADE = 2, 'Purchese Made'
        PAID = 3, 'Paid'
        DELIVERED = 4, 'Delivered'

    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='purchase')
    status = models.IntegerField(choices=StatusPurchase.choices, default=StatusPurchase.CART)

    class Meta:
        db_table = "tb_purchase"
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"
    
    def __str__(self):
        return str(self.user)

    
class ItemPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='itens')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='itens')
    amout = models.IntegerField()

    class Meta:
        db_table = "tb_item_purchase"
        verbose_name = "Item_Purchase"
        verbose_name_plural = "Itens_Purchases"
    
    def __str__(self):
        return f"{self.purchase} ({self.book})"