# Generated by Django 5.0.2 on 2025-02-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebookapp', '0004_alter_recipe_meal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(default='snack', max_length=20, verbose_name='Тип приема пищи'),
        ),
    ]
