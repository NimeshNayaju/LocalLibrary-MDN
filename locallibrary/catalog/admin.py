from django.contrib import admin
from .models import *


admin.site.register(Genre)

class BookAdmin(admin.ModelAdmin):
	list_display=['title', 'author', 'display_genre']

admin.site.register(Book, BookAdmin)

admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'date_of_birth', 'date_of_death']

admin.site.register(Author, AuthorAdmin)


