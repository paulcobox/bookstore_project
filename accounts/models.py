from django.db import models
from django.contrib.auth.models import AbstractUser
from util.models import LegalBaseModel
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser, LegalBaseModel):

  email = models.EmailField('Correo', unique=True, error_messages={
    'unique': 'Un usuario con este correo, ya existe.',
    'required': 'Por favor este campo es requerido.',
    'invalid': 'Por favor, ingrese un valido correo.',
  })

  # phone_regex = RegexValidator(
  #   regex=r'\+?1?\d{9,15}$',
  #   message="Numero de telefono debe de ser ingresado en formato: +5199999999. Solo 11 digitos"
  # )

  # phone_number = models.CharField('Celular',validators=[phone_regex], max_length=17, blank=True)

  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = ['username']

  is_verified = models.BooleanField('verified', default=False, help_text='set to true when the user is verified by email')


class Profile(LegalBaseModel):
  
  user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
  picture = models.ImageField('profile picture', upload_to='accounts/pictures', blank=True, null=True)
  biography = models.TextField(max_length=500, blank=True)


  def __str__(self):
    return str(self.user) 





    