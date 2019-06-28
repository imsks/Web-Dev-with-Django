from django import forms
from first_app.models import userDetails

class NewUserForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = '__all__'
