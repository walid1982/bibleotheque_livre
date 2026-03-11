from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm


def index(request):
    context = {
        "categories": Category.objects.all(),
        "books": Book.objects.all(),
    }
    return render(request, "pages/index.html", context)


def books(request):
    context = {
        "categories": Category.objects.all(),
        "books": Book.objects.all(),
    }
    return render(request, "pages/books.html", context)

def update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books")  # ou "index" selon tes urls
    else:
        form = BookForm(instance=book)

    return render(request, "pages/update.html", {"form": form, "book": book})

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect("books")  # ou "index" selon tes urls
    return render(request, "pages/delete.html", {"book": book})