""" install modules """
from django import forms


class SearchForm(forms.Form):
    """search form class to convert into html form"""

    SEARCH_CHOICES = (("1", "title"), ("2", "contributor"))
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "title or contributor.",
            }
        ),
        required=False,
        min_length=3,
    )
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)
