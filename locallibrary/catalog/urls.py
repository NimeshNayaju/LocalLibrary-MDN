from django.conf.urls import url
from catalog import views

app_name = 'catalog'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.BookListView.as_view(), name='books'),
]

