from django.contrib import admin
from reviews.models import Publisher, Book, BookContributor, Contributor, Review


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ("title", Book.isbn13)
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", "isbn", "publisher__name")


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review Comment", {"fields": ("comment", "rating")}),
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("last_name__startswith", "first_name")
    list_filter = ("last_name",)


admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Review, ReviewAdmin)
