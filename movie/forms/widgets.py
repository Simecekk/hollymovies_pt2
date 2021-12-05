from django import forms


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


class BootstrapEmailInput(forms.EmailInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'form-control'})
        super(BootstrapEmailInput, self).__init__(attrs=attrs)
