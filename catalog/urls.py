from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_card
from catalog.views import ProductListView, BlogRecordListView, BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView, BlogRecordDetailView


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    # path('product_card/', product_card, name='product_card')
    path('product_card/', ProductListView.as_view(), name='product_card'),  #
    path('blog_record/', BlogRecordListView.as_view(), name='blog_record'),
    path('create/', BlogRecordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogRecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', BlogRecordDetailView.as_view(), name='detail')

]