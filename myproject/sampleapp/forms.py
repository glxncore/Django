from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Customer

def validate_not_gmail(value):
    if '@gmail' in value:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value': value},
        )

class LoginModelForm(forms.ModelForm):

    email = forms.CharField(
        max_length=100,
        min_length=10,
        validators=[validate_email, validate_not_gmail]
    )

    password = forms.CharField(
        max_length=50,
        min_length=6
    )

    class Meta:
        model = Customer
        fields = '__all__'