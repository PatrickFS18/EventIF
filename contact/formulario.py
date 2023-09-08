from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField(required=False)
    mail = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
