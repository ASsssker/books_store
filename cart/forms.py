from django import forms

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class AddBookForm(forms.Form):
    quantity = forms.TypedChoiceField( label='Количество', choices=QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)