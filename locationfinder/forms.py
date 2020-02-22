from django import forms
from locationfinder.models import reg


class regform(forms.ModelForm):
    class Meta():
        model = reg
        fields = "__all__"




