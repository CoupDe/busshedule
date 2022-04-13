# Generated by Django 4.0.4 on 2022-04-12 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220325_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='num_bus',
            field=models.CharField(help_text='Формат X777xx777', max_length=50, unique=True, verbose_name='Гос. номер ТС'),
        ),
        migrations.AlterField(
            model_name='routenumber',
            name='num_route',
            field=models.PositiveIntegerField(error_messages={'Error': 'Максимально допустимое значение номера маршрута не более шести символов'}, unique=True, validators=[django.core.validators.MaxValueValidator(99, message=555)], verbose_name='Номер маршрута'),
        ),
    ]