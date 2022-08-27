from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the publisher')
    website = models.URLField(help_text='The website of the publisher')
    email = models.EmailField(help_text='The contact email of the publisher')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text='The title of the book')
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=13, verbose_name='The ISBN of the book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

    def isbn13(self):
        return f'{self.isbn[0:3]}-{self.isbn[3:4]}-{self.isbn[4:6]}-{self.isbn[6:12]}-{self.isbn[12:13]}'

    def __str__(self):
        return self.title


class BookContributor(models.Model):


    class ContributionRole(models.TextChoices):

        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co_Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    role = models.CharField(verbose_name='The role the contributor had in the book', choices=ContributionRole.choices, max_length=20)


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text='The contributor\'s first name')
    last_name = models.CharField(max_length=50, help_text='The contributor\'s last name')
    email = models.EmailField(help_text='The contact email of the contributor')

    def __str__(self):
        return self.first_name


class Review(models.Model):
   comment = models.TextField(help_text='The review comment')
   rating = models.IntegerField(help_text='The rating the reviewer has given')
   date_created = models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created')
   date_edited = models.DateTimeField(null=True, help_text='The date and time the review was last edited')
   creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, help_text='The creator of the review')
   book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text='The book that this review is for')
