from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Entry(models.Model):
    """Модель 'Запись'"""

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="diary/", **NULLABLE, verbose_name="Изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(default=True, verbose_name="Публикация")
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    views_counter = models.PositiveIntegerField(verbose_name="Счётчик просмотров", default=0)

    owner = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name="Пользователь")

    def str(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["title", "content", "publication_sign"]
