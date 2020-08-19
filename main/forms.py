from django import forms
class CreateNewList(forms.Form):
    name=forms.CharField(label='name',max_length=299)
    check=forms.BooleanField(required=False)
