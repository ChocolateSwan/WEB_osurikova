from django.db import models

# Create your models here.


class Question(models.Model):
    header = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        verbose_name='Заголовок вопроса')