from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=100, help_text='Enter a Book Genre (e.g Science Fiction, French Poetry, etc)')


	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN', max_length=13. help_text='Enter the 13 digits ISBN number')
	genre = models.ManyToManyField(Genre, help_text='Select the genre of the book')

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model)
