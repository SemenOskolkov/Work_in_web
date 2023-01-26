from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html')


def product_card(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/product_card.html', context)