from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Genre(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Ficion, French Poetry, etc.)')

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=200, help_text="Enter the book's natural language")		

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=200)		
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	# Author as a string rather than object because it hasn't been declared yet in the file
	summary = models.TextField(max_length=1000, help_text='Enter a brief descrption of the book')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN Number')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
	language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
	# Genre has been defined so we can specify the object

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('catalog:book-detail', kwargs={'pk':self.pk})

	def display_genre(self):
		# This creates a string for genre. This is required to display genre in Admin	
		return ', '.join([genre.name for genre in self.genre.all()[:3]])

	display_genre.short_description = 'Genre'	


import uuid # Required for unique book instances

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for the particular book across the entire library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False	

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On Loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

	class Meta:
		ordering = ['due_back']
		permissions = (('can_marked_returned', 'Set book as returned'), )

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.title)	
		

class Author(models.Model):
	first_name = models.CharField(max_length=100)				
	last_name = models.CharField(max_length=100)				
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('catalog:author-detail', args=[str(self.id)])	

	def __str__(self):
		return '{0}, {1}'.format(self.last_name,self.first_name)	




		








