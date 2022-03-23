from operator import truediv
from tabnanny import verbose
from django.core import validators

from django.db import models

# Create your models here.


class RouteOrder(models.Model):
    title = models.CharField(
        max_length=20, default="Маршрут", verbose_name="Название маршрута")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name_plural = "Маршруты"  # Название модели во множественном числе
        verbose_name = "Маршрут"  # Название модели в удобочитаемом формате
        # ordering = ['']     #сортировка модели по умолчанию

    def __str__(self) -> str:  # возвращает читаемое поле
        return self.title


class BusRoute(models.Model):
    route_order = models.ForeignKey(
        RouteOrder, on_delete=models.PROTECT, default=000, verbose_name="Название маршрута")
    num_route = models.PositiveSmallIntegerField(
        null=False, unique=True, default=000, validators=[validators.MaxLengthValidator(6)])  # Проверить работает ли валидатор
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name_plural = "Номера маршрутов"
        verbose_name = "Номер маршрута"
        # ordering = ['']

    def __str__(self) -> str:  # возвращает читаемое поле
        return self.num_route


class TripTicket(models.Model):
    num_ticket = models.PositiveSmallIntegerField(
        null=False, unique=True, default=000)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name_plural = "Путевые листы"
        verbose_name = "Путевой лист"
        # ordering = ['']


class TimeDeparture(models.Model):
    primary_time = models.TimeField(null=True)
    secondary_time = models.TimeField(null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name_plural = "Время по расписанию"
        verbose_name = "Время по расписанию"
        # ordering = ['']


class DepartureProcess(models.Model):
    pass

    class Meta:
        verbose_name_plural = "Номера по расписанию"
        verbose_name = "Номер по расписанию"
        # ordering = ['']


class Driver(models.Model):
    # Нужна расшифровка категорий
    BW = "БВ"
    MW = "МВ"
    OBW = "ОБВ"
    DRIVER_CATEGORY_CHOICES = [
        (None, "Категория")
        (BW, "БВ"),
        (MW, "МВ"),
        (OBW, "ОБВ"),
    ]
    first_name = models.models.CharField(
        max_length=50, db_index=True, verbose_name="Имя")
    last_name = models.models.CharField(
        max_length=50, db_index=True, verbose_name="Фамилия")
    driver_category = models.CharField(
        max_length=30, choices=DRIVER_CATEGORY_CHOICES, default="Категория не указана")

    class Meta:
        verbose_name_plural = "Водители"
        verbose_name = "Водитель"
        ordering = ['last_name']


class Shift(models.Model):
    pass

    class Meta:
        verbose_name_plural = "Смены"
        verbose_name = "Смена"
        # ordering = ['']


class Bus(models.Model):
    pass

    class Meta:
        verbose_name_plural = "Автобусы"
        verbose_name = "Автобус"
        # ordering = ['']
