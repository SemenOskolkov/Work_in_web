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
    path('prod_create/', ProductCreateView.as_view(), name='prod_create'),
    # path('update/<int:pk>/', ProductUpdateView.as_view(), name='prod_update'),
    path('prod_update/<int:pk>/subjects/', ProductUpdateWithVersionView.as_view(), name='update_with_version'),
    path('prod_delete/<int:pk>/', ProductDeleteView.as_view(), name='prod_delete'),
    path('prod_detail/<int:pk>/', ProductDetailView.as_view(), name='prod_detail'),

    path('prod_status/<int:pk>/', change_status, name='prod_status'),

    path('blog_record_list/', BlogRecordListView.as_view(), name='blog_record_list'),
    path('blog_create/', BlogRecordCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogRecordUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='blog_delete'),
    path('blog_detail/<int:pk>/', BlogRecordDetailView.as_view(), name='blog_detail'),

    path('blog_status/<int:pk>/', change_status, name='blog_status')

]