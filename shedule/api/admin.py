from re import search
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *


# Register your models here.


admin.site.register([RouteOrder, RouteNumber, TripTicket,
                    TimeDeparture, DepartureProcess])


# Добавление в редактор полей из модели ребенка
class DriverInline (admin.TabularInline):
    model = Driver

# Подключение редактируемого класса в панели адм. необходимо включать в кортеж
# admin.site.register(Driver, DriverAdmin)
#  ИЛИ через декоратор


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('num_shift', 'time_create')
    inlines = [DriverInline, ]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'driver_category', 'shift_link')
    search_fields = ('last_name', 'first_name', 'driver_category')

    # Это функциональное поле, можно объединять данные или проводить манипуляци с данными, так-же можно подгрузить __str__
    def shift_link(self, driver):
        if (driver.shift):
            print(type(driver.shift))
            print(driver.shift)
            url = reverse("admin:api_shift_change", args=[driver.shift.id])
            link = '<a href={}>{}</a>'.format(url, driver.shift.num_shift)
            print('xxxx', link)
            return mark_safe(link)
    shift_link.short_description = 'Номер смены'

    @admin.display(
        ordering='last_name',
        description='ФИО',
    )
    def full_name(self, driv):
        return '{} {}'.format(driv.last_name, driv.first_name)


@admin.register(Bus)
class BusrAdmin(admin.ModelAdmin):
    list_display = ('bus_model', 'num_bus', 'bus_category')
    search_fields = ('last_name', 'first_name', 'driver_category')

    def full_name(self, bus):
        return '{} {}'.format(bus.bus_model, bus.num_bus)
