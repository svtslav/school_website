from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    login = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE, verbose_name="Логин (пользователь)")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    photo = models.FileField(verbose_name='Фотография', blank=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    office = models.CharField(max_length=100, verbose_name='Кабинет')
    education = models.CharField(max_length=500, verbose_name='Образование', blank=True)
    teaching_experience = models.CharField(max_length=200, verbose_name='Педагогический стаж', blank=True)

    def full_name(self):
        if self.middle_name:
            return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
        else:
            return self.last_name + ' ' + self.first_name

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name', 'middle_name']
