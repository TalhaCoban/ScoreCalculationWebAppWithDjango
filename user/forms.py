from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Kullanıcı Adı",
        widget=forms.TextInput(attrs={
            'class' : 'RegisterForm',
            "placeholder" : "Kullanıcı Adı:"
        })
    )
    password = forms.CharField(
        label = "Parola",
        widget=forms.TextInput(attrs={
            'class' : 'RegisterForm',
            "type" : "password",
            "placeholder" : "Parola:"
        })
    )


class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=25,
    label="Kullanıcı Adı",
    widget=forms.TextInput(attrs={
        'class' : 'RegisterForm',
        "placeholder" : "Kullanıcı Adı:"
        })
    )
    password = forms.CharField(
        max_length=20,
        label="Parola", 
        widget=forms.TextInput(attrs={
        'class' : 'RegisterForm',
        "type" : "password",
        "placeholder" : "Parola:"
        })
    )
    confirm = forms.CharField(
        max_length=20, 
        label="Parolayı Doğrula",
        widget=forms.TextInput(attrs={
        'class' : 'RegisterForm',
        "type" : "password",
        "placeholder" : "Parolayı Doğrulayın:"
        })
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm  = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor..")
        
        values = {
            "username" : username,
            "password" : password,
        }
        return values
