from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the pages index.")
    test ={
        'name':'hghg',
        'age': 1234567890
    }
    return render(request, 'pages/update.html',  test)
