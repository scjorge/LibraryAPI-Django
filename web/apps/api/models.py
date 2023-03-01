from django.db import models


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
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='publisher')

    class Meta:
        db_table = "tb_book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        return str(self.title)