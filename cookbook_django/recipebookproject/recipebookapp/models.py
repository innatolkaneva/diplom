from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CheckConstraint, Q
from django.db.models.functions import Lower


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'  # переопределение поля идентификации
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(unique=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(email=Lower("email")), name="user_email_lower"),
        ]


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(null=True, upload_to='recipes/', blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    meal_type = models.CharField(
        max_length=20,
        default='snack',
        verbose_name='Тип приема пищи'
    )

