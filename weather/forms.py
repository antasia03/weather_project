from django import forms


class CityForm(forms.Form):
    city = forms.CharField(
        max_length=100,
        label='City',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the city',
        })
    )
