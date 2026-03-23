from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm, CategoryForm


def index(request):
    title = request.GET.get("search_name", "").strip()
    books = Book.objects.all()

    if title:
        books = books.filter(title__icontains=title)

    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        add_category = CategoryForm(request.POST)

        if add_category.is_valid():
            add_category.save()

        if add_book.is_valid():
            add_book.save()
            return redirect("/")  # evite la re-soumission du formulaire au refresh

    context = {
        "categories": Category.objects.all(),
        "books": books,  # <- important
        "form": BookForm(),
        "category_form": CategoryForm(),
        "all_books": Book.objects.filter(active=True).count(),
        "bookssold": Book.objects.filter(status="sold").count(),
        "booksrented": Book.objects.filter(status="rented").count(),
        "booksavailable": Book.objects.filter(status="available").count(),
    }
    return render(request, "pages/index.html", context)


def books(request):
    title = request.GET.get("search_name", "").strip()
    books_queryset = Book.objects.all()

    if title:
        books_queryset = books_queryset.filter(title__icontains=title)

    context = {
        "categories": Category.objects.all(),
        "books": books_queryset,
        #"form": BookForm(),
    }
    #return render(request, "pages/index.html", context)
    return render(request, "pages/books.html", context) # ou "index.html" selon tes urls

def update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/")  # ou "index" selon tes urls
    else:
        form = BookForm(instance=book)

    return render(request, "pages/update.html", {"form": form, "book": book})

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect("/")  # ou "index" selon tes urls
    return render(request, "pages/delete.html", {"book": book})