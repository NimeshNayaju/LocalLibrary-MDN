from django.conf.urls import url
from catalog import views

app_name = 'catalog'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# Book List and Details Page
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book-detail'),

	# Author List and Details Page
	url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
	url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author-detail'),	
]

