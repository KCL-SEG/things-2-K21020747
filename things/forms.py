"""Forms of the project."""

# Create your forms here.

from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label = "Name", max_length = 35)
    description = forms.CharField(widget=forms.Textarea(), label = "Description", max_length = 120)
    quantity = forms.IntegerField(widget=forms.NumberInput(),
                                    validators=[MinValueValidator(0),
                                    MaxValueValidator(50)])
