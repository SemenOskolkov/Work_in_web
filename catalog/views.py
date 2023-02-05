from django.shortcuts import render
from catalog.models import Product, BlogRecord
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


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


class ProductListView(ListView):
    model = Product


def get_counter(requests):
    if requests.method == "GET":
        g = BlogRecord.views_controller
        g += 1
        context = {"g": g}
        return render(requests, context)


class BlogRecordListView(ListView):
    model = BlogRecord


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = {'title', 'content', 'preview', 'sign_publication'}
    succsess_url = reverse_lazy('catalog:blog_record')


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = {'title', 'content', 'preview', 'sign_publication'}
    succsess_url = reverse_lazy('catalog:update')


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    succsess_url = reverse_lazy('catalog:blog_record')


class BlogRecordDetailView(DetailView):
    model = BlogRecord