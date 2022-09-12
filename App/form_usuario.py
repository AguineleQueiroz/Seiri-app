from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

# checa se o nome de usuario e email são unicos
nome_usuario_naoaceitos = ['abc']
User = get_user_model()

class FormCadastro(forms.Form):
    username = forms.CharField(
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

    def nome_usuario_unico(self):
        username = self.cleaned_data.get("username")
        lista_nome_usuarios = User.objects.filter(username__iexact=username)
        if username in nome_usuario_naoaceitos:
            raise forms.ValidationError("Nome de usuário inválido.")
        if lista_nome_usuarios.exists():
            raise forms.ValidationError("Nome de usuário inválido.")
        return username
    
    def email_unico(self):
        email = self.cleaned_data.get("email")
        lista_emails = User.objects.filter(email__iexact=email)
        if lista_emails.exists():
            raise forms.ValidationError("Este E-mail já está em uso.")
        return email



class FormLogin(forms.Form):
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
        lista_nome_usuarios = User.objects.filter(username__iexact=username) # se MeuUsername == meuusername
        if not lista_nome_usuarios.exists():
            raise forms.ValidationError("Usuário inválido.")
        if lista_nome_usuarios.count() != 1:
            raise forms.ValidationError("Usuário inválido.")
        return username

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']