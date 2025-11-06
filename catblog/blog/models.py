from django.db import models
from django.contrib.auth import get_user_model

# Получем пользователя
User = get_user_model()


class Category(models.Model):
    """Модель для определения категории"""
    name = models.CharField(
        verbose_name='Категория'
    )
    slug = models.SlugField(
        max_length=128,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Максимальная длина строки — 128 символов'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Заголовок',
        help_text='Максимальная длина строки — 128 символов'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем'
        ' — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        verbose_name='Категория',
        related_name='posts'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='blog_images',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
