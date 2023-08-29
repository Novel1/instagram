# Generated by Django 4.2.4 on 2023-08-23 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления'),
        ),
        migrations.AddField(
            model_name='post',
            name='edited_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время редактирования'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
    ]
