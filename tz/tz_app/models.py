from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name="Категория")
    amount = models.IntegerField(verbose_name='Количество', validators=[
        MinValueValidator(0, message="Количество не может быть меньше нуля"),
        MaxValueValidator(
            100000, message="Количество не может быть больше 100000")
    ])
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[
                                MinValueValidator(0.0, message="Цена не может быть меньше нуля")])

    def __str__(self):
        return self.title

    def get_categories(self):
        return self.category.get_all_parent_categories()

    class Meta:
        ordering = ['price']


class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name="Родитель", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_all_parent_categories(self):
        if self.parent:
            return f"{self.title} · {self.parent.get_all_parent_categories()}"
        return self.title
