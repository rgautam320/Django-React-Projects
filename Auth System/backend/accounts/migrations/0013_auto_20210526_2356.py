# Generated by Django 3.2.2 on 2021-05-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210521_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]