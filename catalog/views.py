from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from catalog.forms import ProductForm
from catalog.models import Product, BlogRecord, Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html')


# def product_card(request):
#     context = {
#         'object_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_card.html', context)


class ProductListView(ListView):
    model = Product

    # def get_context_data(self, **kwargs):
    #     pass


class ProductCreateView(CreateView):
    model = Product
    # fields = {'product_name', 'description', 'preview', 'purchase_price'}
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)  # Подготовиться обьект с данными из формы
            self.object.owner = self.request.user  # В поле user_create запишится пользователь который делает запрос
            self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    # fields = {'product_name', 'description', 'preview', 'purchase_price'}
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        prod = self.get_object()
        return prod.user == self.request.user or self.request.user.has_perms(['catalog.set_published_status_products',
                                                                              'catalog.can_change_description',
                                                                              'catalog.can_change_category'])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product

    def get_product_from_cache(self):
        queryset = Product.objects.all()
        if settings.CACHE_ENABLED:
            key = f'product_detail_{self.object.pk}'
            cache_data = cache.get(key)
            if cache_data is None:
                cache_data = queryset
                cache.set(key, cache_data)

            return cache_data

        return queryset


# @cache_page
# def detail_controller(request):
#     context = {
#
#     }
#
#     return render(
#         request, 'catalog/product_detail.html',
#         context
#     )


class CategoryListView(ListView):
    model = Category

    def get_categories_from_cache(self):
        queryset = Category.objects.all()
        if settings.CACHE_ENABLED:
            key = 'category'
            cache_data = cache.get(key)
            if cache_data is None:
                cache_data = queryset
                cache.set(key, cache_data)

            return cache_data

        return queryset


def change_status(requests, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.status == Product.STATUS_INACTIV:
        product_item.status = Product.STATUS_ACTIV
    else:
        product_item.status = Product.STATUS_ACTIV
    product_item.save()
    return redirect(reverse('catalog:product_list'))


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_publication=BlogRecord.STATUS_ACTIVE)
        return queryset


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = {'title', 'content', 'preview', 'sign_publication'}
    success_url = reverse_lazy('catalog:blog_record_list')


class BlogRecordUpdateView(UserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.blog_change'
    model = BlogRecord
    fields = {'title', 'content', 'preview', 'sign_publication'}
    success_url = reverse_lazy('catalog:blog_record_list')

    def test_func(self):
        blog = self.get_object()
        return blog.user == self.request.user.has_perm('catalog.set_published_status_blog')


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('catalog:blog_record_list')


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_counter(self):
        obj = super().get_counter()
        obj.blog_view += 1
        obj.save()
        return obj


def change_status(requests, pk):
    blog_item = get_object_or_404(BlogRecord, pk=pk)
    if blog_item.status == BlogRecord.STATUS_INACTIV:
        blog_item.status = BlogRecord.STATUS_ACTIV
    else:
        blog_item.status = BlogRecord.STATUS_ACTIV
    blog_item.save()
    return redirect(reverse('catalog:blog_record_list'))
