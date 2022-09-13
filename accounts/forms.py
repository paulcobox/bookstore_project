# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

  captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')


  def clean_captcha_answer(self):
        data = self.cleaned_data['captcha_answer']
        if not (str(data).isdigit() and  int(data)==4):
            raise ValidationError("La suma es incorrecta.")
        return data

  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields = ('email',) # new

    
