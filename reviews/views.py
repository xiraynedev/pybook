"""import modules"""
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contributor
from .utils import average_rating
from .forms import SearchForm


def index(request):
    """main route for reviews app"""
    return render(request, "base.html", {"title": "PyBook"})


def books(request):
    """the books route to handle retrieving all books and information"""
    all_books = Book.objects.all()
    all_books_list = []

    for book in all_books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        all_books_list.append(
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews,
            }
        )

    context = {"books_list": all_books_list}

    return render(request, "books_list.html", context)


def book_details(request, book_id):
    """return the details template for the all_books"""
    book = get_object_or_404(Book, id=book_id)

    reviews = book.review_set.all()

    overall_rating = average_rating([review.rating for review in reviews])

    context = {
        "book": book,
        "overall_rating": overall_rating,
        "reviews": reviews,
    }

    return render(request, "book_details.html", context)


def book_search(request):
    """return a search form to the client"""
    form = SearchForm()

    return render(request, "book_search.html", {"form": form})


def results(request):
    """process the search form results"""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["search_in"] == "1":
                try:
                    book = Book.objects.filter(
                        title__icontains=form.cleaned_data["search"]
                    )
                    if len(book) == 0:
                        raise Exception()

                except:
                    return render(
                        request, "error.html", {"error": "No book was found."}
                    )
            elif form.cleaned_data["search_in"] == "2":
                try:
                    contributor = Contributor.objects.get(
                        first_name__icontains=form.cleaned_data["search"]
                    )
                    book = contributor.book_set.all()

                except:
                    return render(
                        request,
                        "error.html",
                        {
                            "error": "No contributor was found.",
                        },
                    )
    else:
        form = SearchForm()

    return redirect(reverse(book_details, kwargs={"book_id": book[0].id}))
