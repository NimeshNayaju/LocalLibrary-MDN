from django.shortcuts import render
from .models import *
from django.views.generic import *


def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()

	# Get a session value, setting a default if it is not present ('0')
	num_visits = request.session.get('num_visits', 0)
	# Update the session value
	request.session['num_visits'] = num_visits+1

	return render(request, 'index.html',
		context={
		'num_books':num_books, 
		'num_instances':num_instances, 
		'num_instances_available':num_instances_available, 
		'num_authors':num_authors,
		'num_visits':num_visits},
		)


# Book List and Details
class BookListView(ListView):
	model = Book
	paginate_by = 5

class BookDetailView(DetailView):
	model = Book
	
# Author List and Details	
class AuthorListView(ListView):
	model = Author
	paginate_by = 5

class AuthorDetailView(DetailView):
	model = Author	


