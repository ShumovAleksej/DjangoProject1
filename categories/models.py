from django.db import models

class Categories(models.Model):
    category_id = models.CharField(max_length=10)
    parent_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Одна строка таблицы CATEGORIES: название: {self.name}, собственный код: {self.category_id}, родителький \
        код: {self.parent_id}'

class Offers(models.Model):
    name = models.CharField(max_length=500)
    self_id = models.CharField(max_length=10)
    category_id = models.CharField(max_length=10)
    picture = models.CharField(max_length=500, default='')

    class Meta:
        indexes = [
            models.Index(fields=['self_id'], name='self_id_idx'),
        ]

# Create your models here.
