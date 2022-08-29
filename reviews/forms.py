from django import forms


class SearchForm(forms.Form):
    SEARCH_CHOICES = (('1', 'title'), ('2', 'contributor'))
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)