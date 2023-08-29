from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    descriptions = models.CharField(verbose_name='Описание', null=True, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    likes_count = models.IntegerField(verbose_name='Количество лайков', default=0)
    comments_count = models.IntegerField(verbose_name='Количество коментариев', default=0)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время редактирования"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удален",
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return self.user

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE, verbose_name='Публикация')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='author_like', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='post_like', null=False,
                             blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )