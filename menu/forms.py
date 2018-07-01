from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient
from datetime import datetime
from django.core import validators
from django.utils import timezone

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('season', 'items', 'expiration_date')


    def clean_expiration_date(self):
        """validates that expiration_date"""

        expiration_date = self.cleaned_data.get('expiration_date', None)
        try:
            if expiration_date >= timezone.now():
                return expiration_date
            else:
                raise forms.ValidationError("""Expiration date must be
                                            after creation of menu""")
        except TypeError:
            raise forms.ValidationError('Please enter an expiration date')
