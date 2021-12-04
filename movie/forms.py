from django import forms


class DummyForm(forms.Form):
    int_field = forms.IntegerField(min_value=5, max_value=10)
    username = forms.CharField(required=False, empty_value='unknown', label='Dummy Username')
