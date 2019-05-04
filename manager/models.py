from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(unique=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Solution(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(unique=True)
    topic = models.ForeignKey(Topic, blank=True, null=True, default=None, on_delete=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class SolutionImage(models.Model):
    image = models.ImageField(upload_to='solution_images/')
    solution = models.ForeignKey(Solution, blank=True, null=True, default=None, on_delete=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картинки'


class SolutionRating(models.Model):
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    solution = models.ForeignKey(Solution, blank=True, null=True, default=None, on_delete=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'