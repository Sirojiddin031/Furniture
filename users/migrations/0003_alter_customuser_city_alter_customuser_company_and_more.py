# Generated by Django 5.1.5 on 2025-02-08 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.MaxLengthValidator(100), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.RegexValidator('^\\+?\\d{1,15}$', message='Phone number must be numeric and can include a leading "+"')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.MinLengthValidator(2)]),
        ),
    ]
