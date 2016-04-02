from django import forms
from .models import Join


class EmailForm(forms.Form):
    Name = forms.CharField(required=False)
    Email = forms.EmailField()


class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email']
