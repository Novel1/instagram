from django import forms
from django.contrib.auth import get_user_model

from posts.models import Post


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Email')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)


class CustomUserCreateForm(forms.ModelForm):
    GENDER_CHOICE = [
        ('Man', 'Man'),
        ('Women', 'Women'),
        ('Other', 'Other')
    ]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICE)
    password = forms.CharField(required=True, label='Password', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(required=True, label='Confirm password', strip=False, widget=forms.PasswordInput)
    inform = forms.CharField(required=False, label='Information')
    phone = forms.CharField(label='Phone')
    username = forms.CharField(label='Login')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    language = forms.CharField(label='Language', required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'email', 'password', 'password_confirm', 'first_name', 'birth_date', 'phone',
                  'inform', 'gender', 'avatar', 'language')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password mismatch!')

    def save(self, commit=True):
        user = super().save(commit=False)
        print(user)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'email', 'avatar', 'birth_date', 'username')
        labels = {'first_name': 'name', 'last_name': 'last_name', 'email': 'Email'}


class PostForm(forms.ModelForm):
    descriptions = forms.CharField(required=False, label='Описание')

    class Meta:
        model = Post
        fields = ('descriptions', 'image',)
        labels = {
            'image': 'Фото',
            'descriptions': 'Описание'
        }