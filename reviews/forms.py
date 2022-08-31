from django import forms
from .models import Publisher


class SearchForm(forms.Form):

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


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
