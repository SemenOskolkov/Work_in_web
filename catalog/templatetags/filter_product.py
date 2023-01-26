import os
from django import template
from catalog.models import Product

register = template.Library()

@register.filter
def mediapath(value):
    return os.path(Product.self.preview)

@register.simple_tag
def mediapath(value):
    return os.path(Product.self.preview)

