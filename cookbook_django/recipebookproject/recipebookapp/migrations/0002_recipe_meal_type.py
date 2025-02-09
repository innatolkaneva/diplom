# Generated by Django 5.0.2 on 2025-02-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('breakfast', 'Завтрак'), ('snack', 'Перекус'), ('lunch', 'Обед'), ('dinner', 'Ужин')], default='breakfast', max_length=10),
            preserve_default=False,
        ),
    ]
