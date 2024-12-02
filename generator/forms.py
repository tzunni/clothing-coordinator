# generator/forms.py
from django import forms
from .models import Item, Weather, Shade

class ItemChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'data-name': lambda item: item.name,
            'data-weather': lambda item: item.weather.name,
            'data-shade': lambda item: item.shade.name,
        })
        return attrs

class ItemForm(forms.ModelForm):
    weather = forms.ModelChoiceField(queryset=Weather.objects.all(), label="Select Weather")
    shade = forms.ModelChoiceField(queryset=Shade.objects.all(), label="Select Shade")
    type = forms.ChoiceField(choices=Item.TYPE_CHOICES, label="Select Type")

    class Meta:
        model = Item
        fields = ['name', 'type', 'weather', 'shade']

class RemoveItemForm(forms.Form):
    item_id = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        label="Select Item to Remove"
    )
