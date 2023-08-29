from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        to=get_user_model(),
        related_name='subscriptions',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    subscribed_to = models.ForeignKey(
        to=get_user_model(),
        related_name='subscribers',
        on_delete=models.CASCADE,
        verbose_name='Подписка'
    )


class Like(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        to='posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Публикация',
        related_name='likes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
