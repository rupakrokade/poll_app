from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    """A Class to create new form for User's Registration.
    It has the various fields and functions required to register
    a new user to the system"""

    username = forms.CharField(max_length=30, help_text='Letters, digits,\
                period and underscores only.')
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self):
        u_name = self.cleaned_data["username"]
        u_name = u_name.lower()
        pwd = self.cleaned_data["password"]
        email = self.cleaned_data['email']
        new_user = User.objects.create_user(u_name, email, pwd)

        new_user.first_name = self.cleaned_data["first_name"]
        new_user.last_name = self.cleaned_data["last_name"]
        new_user.save()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())