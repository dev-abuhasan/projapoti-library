from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Wishlist, Borrowing, Review


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'date_joined')
    search_fields = ('username', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn',
                    'publication_date', 'genre', 'availability')
    list_filter = ('genre',)
    search_fields = ('title', 'author', 'isbn')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'borrow_date', 'return_date', 'book')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'rating', 'book')


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
admin.site.register(Review, ReviewAdmin)
