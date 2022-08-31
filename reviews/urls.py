from django.urls import path
from .views import (
    index,
    books,
    book_details,
    book_search,
    results,
    publishers,
    publisher_edit,
)

urlpatterns = [
    path("", index, name="index_view"),
    path("books/", books, name="book_list_view"),
    path("books/<int:id>", book_details, name="book_details_view"),
    path("search/", book_search, name="book_search_view"),
    path("results/", results, name="results_view"),
    path("publishers/", publishers, name="publishers_view"),
    path("publishers/<int:pk>/", publisher_edit, name="publisher_edit_view"),
    path("publishers/new/", publisher_edit, name="publisher_create_view"),
]
