from django import forms
class Uploadfileform(forms.Form):
    file = forms.FileField()

class update_request_form(forms.Form):
    update = forms.BooleanField(required=False)