from ast import Delete
from operator import truediv
from tabnanny import verbose
from xml.etree.ElementTree import tostring
from django.core import validators

from django.db import models

# Create your models here.
# Нужна расшифровка категорий
BW = 'БВ'
MW = 'МВ'
OBW = 'ОБВ'
CATEGORY_CHOICES = [(None, 'Категория'), (BW, 'БВ'), (MW, 'МВ'), (OBW, 'ОБВ')]


class RouteOrder(models.Model):
    title = models.CharField(
        max_length=20, default='Маршрут', verbose_name='Номер маршрута')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Маршруты'  # Название модели во множественном числе
        verbose_name = 'Маршрут'  # Название модели в удобочитаемом формате
        # ordering = ['']     #сортировка модели по умолчанию

    def __str__(self) -> str:  # возвращает читаемое поле
        return self.title


class RouteNumber(models.Model):
    #    route_order = models.ForeignKey(
 #       RouteOrder, on_delete=models.SET_NULL, null=True,blank=True, default=000, verbose_name='Номер маршрута')
    num_route = models.PositiveIntegerField(
        # Проверить работает ли валидатор
        null=False, unique=True,   validators=[validators.MaxValueValidator(limit_value=999999, message='555')],
        verbose_name='Номер маршрута')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменён')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Номера маршрутов'
        verbose_name = 'Номер маршрута'
        # ordering = ['']

    def __str__(self) -> str:  # возвращает читаемое поле
        return str(self.num_route)


class TripTicket(models.Model):
    num_ticket = models.PositiveSmallIntegerField(
        null=False, unique=True, default=000)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Путевые листы'
        verbose_name = 'Путевой лист'
        ordering = ['num_ticket']


class TimeDeparture(models.Model):
    primary_time = models.TimeField(null=True)
    secondary_time = models.TimeField(null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Время по расписанию'
        verbose_name = 'Время по расписанию'
        # ordering = ['']


class DepartureProcess(models.Model):

    num_ticket = models.PositiveSmallIntegerField(
        null=False, unique=True, default=000)
    driver_category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='Категория не указана')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Номера по расписанию'
        verbose_name = 'Номер по расписанию'
        # ordering = ['']


class Shift(models.Model):
    num_shift = models.PositiveIntegerField(
        null=False, unique=True, default=100, verbose_name='Номер смены')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')
    is_full = models.BooleanField(default=False, verbose_name='Заполнение')

    class Meta:
        verbose_name_plural = 'Смены'
        verbose_name = 'Смена'
        # ordering = ['']

    def __str__(self) -> str:
        return str(self.num_shift)


class Driver(models.Model):

    shift = models.ForeignKey(
        Shift, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Номер смены')
    first_name = models.CharField(
        max_length=50, db_index=True, verbose_name='Имя')
    last_name = models.CharField(
        max_length=50, db_index=True, verbose_name='Фамилия')
    driver_category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='Категория', verbose_name='Категория водителя')

    class Meta:
        verbose_name_plural = 'Водители'
        verbose_name = 'Водитель'
        ordering = ['last_name']

    def __str__(self) -> str:
        return '{} {}'.format(self.last_name, self.first_name)


class Bus(models.Model):
    bus_category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, null=False, verbose_name='Категория автобуса')
    num_bus = models.CharField(max_length=50,
                               null=False, unique=True, verbose_name='Гос. номер ТС', help_text='Формат X777xx777')  # В дальнейшем аписать валидатор для номера
    bus_model = models.CharField(max_length=50,
                                 null=False, default='',  verbose_name='Марка ТС')
    is_fixed = models.BooleanField(default=False, verbose_name='Закреплен')
    route_number = models.ForeignKey(
        RouteNumber, on_delete=models.SET_NULL, null=True, default=000, verbose_name='Номер маршрута')

    class Meta:
        verbose_name_plural = 'Автобусы'
        verbose_name = 'Автобус'
        # ordering = ['']
