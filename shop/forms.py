import json

from django import forms

from shop.models import Product


class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(CartForm, self).__init__(*args, **kwargs)

        for product in items:
            self.fields['id_product_{}'.format(product.id)] = forms.IntegerField(
                initial=1,
                label=product.name,
                required=False
            )
            colors = product.colors_available.all().values_list('name', flat=True)
            self.fields[f'id_product_color_{product.id}'] = forms.ChoiceField(
                choices=[(color, color) for color in colors],
                label='color',
                required=False
            )