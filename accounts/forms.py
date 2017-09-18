from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Этот пользователь не существует!')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль!')
            if not user.is_active:
                raise forms.ValidationError('Этот пользователь не более активен.')
        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email адрес')
    email2 = forms.EmailField(label='Введите повторно Email адрес')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must be same')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has alredy been registred')
        return super(UserRegisterForm, self).clean()