from django import forms

class ListMsgsForm(forms.Form):
    "Basic form for sending list of messages from last msg_id"
    msg_id = forms.IntegerField(min_value=0)

class MsgForm(forms.Form):
    "Basic form for accepting message from author"
    message = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'msg'}))
