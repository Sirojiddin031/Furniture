from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator, EmailValidator

from common.models import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128, validators=[MaxLengthValidator(128)], default=None)
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

class AboutModel(models.Model):
    name = models.CharField(max_length=128, validators=[MaxLengthValidator(128)])
    job = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'