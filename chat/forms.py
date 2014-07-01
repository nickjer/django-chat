from django import forms

class MsgForm(forms.Form):
    "Basic form for accepting message from author"
    author = forms.CharField(max_length=25)
    message = forms.CharField(max_length=200)
