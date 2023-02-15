from django.db import transaction
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from catalog.models import Product, Version
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_with_version.html'

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.pk])


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        formset.instance = self.object

        version_checkboxes = [value.get('is_actual') for value in formset.cleaned_data if
                              value.get('is_actual')]

        with transaction.atomic():
            self.object = form.save()

            if len(version_checkboxes) > 1:
                messages.info(self.request, 'Только одна версия может быть активной')
                return self.form_invalid(form)

            if formset.is_valid():
                formset.save()

        return super().form_valid(form)