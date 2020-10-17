from django import forms

class NounCollectForm(forms.Form):
    text = forms.CharField(label="入力テキスト",required=True)