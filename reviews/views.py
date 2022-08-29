from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Review, Contributor
from .utils import average_rating
from .forms import SearchForm

# Create your views here.
def index(request):
    return render(request, 'base.html', {'title': 'PyBook'})


def book_list(request):
    books = Book.objects.all()
    book_list = []

    for book in books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})

    context = {'book_list': book_list}

    return render(request, 'books_list.html', context)


def book_details(request, id):
    book = get_object_or_404(Book, id=id)

    reviews = book.review_set.all()

    overall_rating = average_rating([review.rating for review in reviews])

    context = {'book': book, 'overall_rating': overall_rating, 'reviews': reviews}

    return render(request, 'book_details.html', context)


def book_search(request):
    form = SearchForm()

    return render(request, 'book_search.html', {'form': form})


def results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['search_in'] == '1':
                try:
                    book = Book.objects.filter(title__icontains = form.cleaned_data['search'])

                    if len(book) == 0:
                        raise Exception()

                except:
                    return render(request, 'error.html', {'error': 'No book was found.'})
            elif form.cleaned_data['search_in'] == '2':
                try:
                    contributor = Contributor.objects.get(first_name__icontains = form.cleaned_data['search'])
                    book = contributor.book_set.all()

                except:
                    return render(request, 'error.html', {'error': 'No contributor was found.'})
    else:
        form = SearchForm()

    return render(request, 'search_results.html', {'book': book[0]})
