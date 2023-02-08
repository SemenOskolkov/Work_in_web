from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, change_status
from catalog.formset_views import ProductUpdateWithVersionView
from catalog.views import BlogRecordListView, BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView, BlogRecordDetailView
from catalog.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    # path('product_card/', product_card, name='product_card')
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='prod_create'),
    # path('update/<int:pk>/', ProductUpdateView.as_view(), name='prod_update'),
    path('update/<int:pk>/subjects/', ProductUpdateWithVersionView.as_view(), name='update_with_version'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='prod_delete'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='prod_detail'),

    path('status/<int:pk>/', change_status, name='prod_status'),

    path('blog_record/', BlogRecordListView.as_view(), name='blog_record_list'),
    path('create/', BlogRecordCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogRecordUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='blog_delete'),
    path('detail/<int:pk>/', BlogRecordDetailView.as_view(), name='blog_detail'),

    path('status/<int:pk>/', change_status, name='blog_status')

]