from django import forms
class ReservationForm(forms.Form):
    name=forms.CharField(max_length=15)
    city=forms.CharField(max_length=15)
    Places=forms.ChoiceField(choices=[(1, 1),(2, 2)])
    Category=forms.ChoiceField(choices=[('enfant', 'enfant'),('adult', 'adult')])
    