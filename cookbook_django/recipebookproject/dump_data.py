import os
import sys
import json
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipebookproject.settings')
django.setup()

from django.core import serializers
from recipebookapp.models import Recipe, CustomUser  # 


data = []

users = CustomUser.objects.all()
for user in users:
    data.append({
        'model': 'recipebookapp.customuser',
        'pk': user.pk,
        'fields': {
            'password': user.password,
            'last_login': str(user.last_login) if user.last_login else None,
            'is_superuser': user.is_superuser,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': str(user.date_joined),
        }
    })

recipes = Recipe.objects.all()
for recipe in recipes:
    data.append({
        'model': 'recipebookapp.recipe',
        'pk': recipe.pk,
        'fields': {
            'title': recipe.title,
            'description': recipe.description,
            'cooking_steps': recipe.cooking_steps,
            'cooking_time': str(recipe.cooking_time),
            'image': str(recipe.image) if recipe.image else None,
            'entry_date': str(recipe.entry_date),
            'is_visible': recipe.is_visible,
            'author_id': recipe.author.id if recipe.author else None,
            'meal_type': recipe.meal_type,
        }
    })


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Данные успешно сохранены в data.json")