from django.shortcuts import render,redirect
from .models import Product
from .froms import ProductForm,RawProductForm
from django.http import Http404
# Create your views here.


#def create_product_view(request):
#    form= RawProductForm()
#    if request.method == "POST":
#        form= RawProductForm(request.POST)
#        if form.is_valid():
#            print(form)
#            #form.save() doesnt work with this form
#            Product.objects.create(**form.cleaned_data)
#            form= RawProductForm()
#    context={
#        "form":form
#    }
#    return render(request, "products/product_create.html", context)
def create_product_view(request):
    form= ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= ProductForm()
    context={
        "form":form
    }
    return render(request, "products/product_create.html", context)

def product_view(request,id):
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context={
        "obj":obj
    }
    return render(request,"products/detail.html",context)


def delete_product_view(request,id):
    try:
        obj= Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    if request.method == "POST":
        obj.delete()
            
    context={
        "obj":obj
    }
    return render(request, "products/product_delete.html", context)


def all_product_view(request):
    query=Product.objects.all()
    context={
        "object_list":query
    }

    return render(request, "products/all_products_delete.html", context)

