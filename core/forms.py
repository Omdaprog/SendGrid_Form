from django import forms

class SendGridForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    email1 = forms.EmailField()
    money = forms.DecimalField()