from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['name']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = "__all__"
        fields = [
            "title",
            "author",
            "photo_author",
            "price", 
            "retal_price_day",
            "pages",
            "photo_book",
            "retal_period",
            "status",
            "category",
            "total_rental",
            ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "photo_author": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "retal_price_day": forms.NumberInput(attrs={"class": "form-control" , "id": "retal_price_day"}),
            "retal_period": forms.NumberInput(attrs={"class": "form-control", "id": "retal_period"}),
            "total_rental": forms.NumberInput(attrs={"class": "form-control", "id": "total_rental"}),
            "pages": forms.NumberInput(attrs={"class": "form-control"}),
            "photo_book": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            
        }
