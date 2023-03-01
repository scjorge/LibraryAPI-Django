from django.contrib import admin

from .models import Author, Book, Category, Publisher, Purchase, ItemPurchase


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Publisher)

class ItensInLine(admin.TabularInline):
    model = ItemPurchase


@admin.register(Purchase)
class AdminPurchase(admin.ModelAdmin):
    inlines = (ItensInLine,)