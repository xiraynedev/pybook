from django.contrib import admin
from reviews.models import Publisher, Book, BookContributor, Contributor, Review


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', Book.isbn13)
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('creator', 'book')}), ('Review Comment', {'fields': ('comment', 'rating')}))

admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Contributor)
admin.site.register(Review, ReviewAdmin)
