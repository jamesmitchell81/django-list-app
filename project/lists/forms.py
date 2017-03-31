from django import forms

class NewListForm(forms.Form):
    widgets = {
        'new_list': forms.TextInput(
            attrs={
                'class': 'list-item-input list-item',
                'autofocus': True
            }
        )
    }
    new_list = forms.CharField(max_length=255, label='', widget=widgets['new_list'])

class NewItemForm(forms.Form):
    widgets = {
        'new_item': forms.TextInput(
            attrs={
                'class': 'list-item-input list-item',
                'autofocus': True
            }
        )
    }
    new_item = forms.CharField(
        max_length=255,
        label='',
        widget=widgets['new_item']
    )

class EditItemForm(forms.Form):
    widgets = {
        'item_value': forms.TextInput(
            attrs={
                'class': 'list-item-input list-item',
                'autofocus': True
            }
        )
    }
    item_value = forms.CharField(
        max_length=255,
        label='',
        widget=widgets['item_value']
    )
    complete = forms.BooleanField(required=False)



