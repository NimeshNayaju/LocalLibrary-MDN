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

# Author create, update and delete
class AuthorCreate(CreateView):
	model = Author
	fields = '__all__'
	initial={'date_of_death':'05/01/2018'}

class AuthorUpdate(UpdateView):
	model = Author	
	fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', ]


from django.urls import reverse_lazy
class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('catalog:authors')	


from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.contrib.auth.mixins import PermissionRequiredMixin

class LoanedBooksAllListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission.
    """
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back') 


from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
import datetime

from django.contrib.auth.decorators import permission_required

from .forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('catalog:all-borrowed') )

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})




