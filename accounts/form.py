from django import forms
from .models import User

# ユーザ作成フォームを継承


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='パスワード（確認用）', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', "email", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
