from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


class Account(AbstractUser):
    GENDER_CHOICES = [
        ('Man', 'Man'),
        ('Women', 'Women'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    inform = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(null=True, blank=True, verbose_name='Phone')
    language = models.CharField(max_length=100, null=True, blank=True, verbose_name='language')
    email = models.EmailField(verbose_name='Email', unique=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pic', verbose_name='Avatar')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Bithday')
    subscribers_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик подписчиков'
    )
    subscriptions_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик подписок'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'







