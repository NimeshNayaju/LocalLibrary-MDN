from django.conf.urls import url
from catalog import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# Book List and Details Page
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book-detail'),

	# Author List and Details Page
	url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
	url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author-detail'),	

	# loaned books
	url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),

	# renew books
	# url(r'^book/(?P<pk>[0-9]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
	path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

	# author create, update and delete
	url(r'^author/create/$', views.AuthorCreate.as_view(), name='author-create'),
	url(r'^author/(?P<pk>[0-9]+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
	url(r'^author/(?P<pk>[0-9]+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),

]

