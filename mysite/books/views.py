from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Book
from books.forms import NameForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def book(request, book_title):
    """
    Display rating screen for the book and modify database book rating and rating_amounts
    :param request:
    :param book_title:
    :return:
    """
    if request.method == 'POST':
        str_rating = request.POST.get("rating", "")
        rating = int(str_rating)
        book_result = Book.objects.get(book_title=book_title)
        current_book_ratings_amount = book_result.ratings_amount
        book_result.ratings_amount += 1
        book_result.book_rating = ((book_result.book_rating * current_book_ratings_amount) + rating)/book_result.ratings_amount
        book_result.save()
        return redirect("/")
    return render(request, "book.html", {"book_title": book_title})


@csrf_protect
def index(request):
    """
    Main view to display books from database. Allows user to create new book and order result asc and desc.
    :param request:
    :return:
    """
    context = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['book_title']
            author = form.cleaned_data["book_author"]
            new_book = Book(book_author=author, book_title=title)
            try:
                new_book.save()
            except IntegrityError:
                context["error"] = "Podany tytuł istnieje już w bazie"

    if search_phrase := request.GET.get("search", ""):
        searched_result = Book.objects.filter(Q(book_title__contains=search_phrase) | Q(book_author__contains=search_phrase))
        context["results"] = searched_result

    else:
        if "order_asc" in request.GET:
            all_results = Book.objects.all().order_by("ratings_amount")
        else:
            all_results = Book.objects.all().order_by("-ratings_amount")
        context["results"] = all_results

    return render(request, 'main.html', context)
