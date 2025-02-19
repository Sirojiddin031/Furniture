from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, validators=[MaxLengthValidator(255), MinLengthValidator(3)])
    company = models.CharField(max_length=255, blank=True, validators=[MaxLengthValidator(255), MinLengthValidator(3)])
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True, validators=[MaxLengthValidator(100), MinLengthValidator(3)])
    postal_code = models.CharField(max_length=20, blank=True, validators=[MaxLengthValidator(20), MinLengthValidator(2)])
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        validators=[
            MaxLengthValidator(20), 
            RegexValidator(r'^\+?\d{1,15}$', message='Phone number must be numeric and can include a leading "+"')
        ]
    )
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'users'
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Bu qatorni qo'shing
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Bu qatorni qo'shing
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )