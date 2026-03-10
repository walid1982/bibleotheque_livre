from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the pages index.")
    return render(request, 'pages/index.html')

def books(request):
    return render (request, 'pages/books.html')