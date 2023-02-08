from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # def clean_product_name(self):
    #     product_name = self.cleaned_data['product_name']
    #     dont_use = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if product_name in dont_use:
    #         raise ValidationError('Запрещенное слово')
    #     return product_name
    #
    # def clean_description(self):
    #     description = self.cleaned_data['description']
    #     dont_use = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if description in dont_use:
    #         raise ValidationError('Запрещенное слово')
    #     return description


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def get_quaryset(self):
        quaryset = super().get_quaryset()
        quaryset = quaryset.filter(status=VersionForm.STATUS_ACTIVE)
        return quaryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'