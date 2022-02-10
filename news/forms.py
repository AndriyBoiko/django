from django import forms
from django.forms import fields
from django.forms.models import model_to_dict
from .models import News
import re 
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField




class ContactForm(forms.Form):
    subject = forms.CharField(label='Tема', widget=forms.TextInput(attrs= {'class': 'form-control'}))
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs= {'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Імя Ваше', widget=forms.TextInput(attrs= {'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs= {'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Імя Ваше', widget=forms.TextInput(attrs= {'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    password2 = forms.CharField(label='Повторити пароль', widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs= {'class': 'form-control'}) ) 

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'in_publisher', 'category']
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs= {'class': 'form-control',  'rows': 5}),
            'category': forms.Select( attrs= {'class': 'form-control'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match (r'\d', title ):
            raise ValidationError('Назва не повинна починатися з цифри')
        return title
    
    
    # title = forms.CharField(max_length = 150, label = 'Заголовок', widget = forms.TextInput(attrs= {'class': 'form-control'}))
    # content = forms.CharField( label = 'Контент', required = False, widget = forms.Textarea(
    #     attrs = 
    #     {
    #         'class': 'form-control', 
    #         'rows': 5
    #     }))
    # in_publisher = forms.BooleanField(label='Опубліковано', initial=True)
    # category = forms.ModelChoiceField(empty_label = 'Виберіть категорію', queryset = Category.objects.all(), label = 'Категорія',  widget = forms.Select(attrs= {'class': 'form-control'}))