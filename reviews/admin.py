from django.contrib import admin
from reviews.models import Publisher, Book, BookContributor, Contributor, Review

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Contributor)
admin.site.register(Review)
