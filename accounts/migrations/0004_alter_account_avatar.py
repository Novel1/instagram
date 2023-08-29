# Generated by Django 4.2.4 on 2023-08-16 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='1.jpg', null=True, upload_to='user_pic/', verbose_name='Avatar'),
        ),
    ]