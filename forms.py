from django import forms
from accounts.models import Profile, User


class UsersManageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']
        