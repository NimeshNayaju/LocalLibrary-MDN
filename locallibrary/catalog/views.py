from django.shortcuts import render
from .models import *
from django.views.generic import *


def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()

	return render(request, 'index.html',
		context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors':num_authors},
		)

class BookListView(ListView):
	model = Book
	context_object_name = 'book_list'
	template_name = 'books/book_list.html'

	def get_queryset(self):
		return Book.objects.filter(title__icontains='valk' [:5])
