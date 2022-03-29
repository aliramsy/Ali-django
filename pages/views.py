from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_user={
        "name":"ali",
        "number":44554,
        "is_active":"True",
        "sales":[12,5,6,9],
    }
    return render(request, "about.html", my_user)