from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

invalid_usernames = ['abc']
User = get_user_model()

class RegisterForm(forms.Form):

    username = forms.CharField(
        label='Name',
        widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "user-email",
                "placeholder": "E-mail adress..."
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "Password"
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password",
                "placeholder": "Confirm password"
            }
        )
    )

    def unique_name_usr(self):
        username = self.cleaned_data.get("username")
        username_list = User.objects.filter(username__iexact=username)
        if username in invalid_usernames:
            raise forms.ValidationError("Invalid user name.")
        if username_list.exists():
            raise forms.ValidationError("Username already exists.")
        return username
    
    def unique_email(self):
        email = self.cleaned_data.get("email")
        email_lst = User.objects.filter(email__iexact=email)
        if email_lst.exists():
            raise forms.ValidationError("This email is already in use.")
        return email



class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "placeholder": "password"
            }
        )
    )

    def nome_usuario_unico(self):
        username = self.cleaned_data.get("username")
        username_lst = User.objects.filter(username__iexact=username)
        if not username_lst.exists():
            raise forms.ValidationError("User does not exist.")
        if username_lst.count() != 1:
            raise forms.ValidationError("Invalid username.")
        return username

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']