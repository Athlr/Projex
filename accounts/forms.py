from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
