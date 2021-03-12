from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from products.forms import ProductForm

# Create your views here.
def home_view (request, *args, **kwargs):
    # ...
    return render(request, "study.html", {})
def checkView(request):
    obj = Product.objects.get(id = 1)
    context = {
        'Title': obj.title,
        'Desc': obj.desc,
        'price': obj.price
    }
    return render(request, "test.html", context)

def product_form(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        Product.objects.create(**form.cleaned_data)
        print(form)
    context = {
        'form' : form
    } 
    return render(request, "test3.html", context)