# Generated by Django 4.2.4 on 2023-08-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_userprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='subscribers_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Счетчик подписчиков'),
        ),
        migrations.AddField(
            model_name='account',
            name='subscriptions_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Счетчик подписок'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
