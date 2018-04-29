from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin


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

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
