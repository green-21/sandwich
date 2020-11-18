from django import forms

class WritePost(forms.Form):
    img_file = forms.ImageField()
    post_msg = forms.CharField(max_length=200)