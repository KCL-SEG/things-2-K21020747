"""Forms of the project."""

# Create your forms here.

from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label = "Name")
    description = forms.CharField(widget=forms.Textarea(), label = "Description")
    quantity = forms.IntegerField(widget=forms.NumberInput())
