from django import forms
from django.contrib.auth.forms import UserCreationForm

from recipebookapp.models import CustomUser, Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label="Наименование блюда",
                            widget=forms.TextInput(attrs={'class': 'recipe-form__title'}))
    description = forms.CharField(max_length=250,
                                  label="Краткое описание блюда",
                                  widget=forms.Textarea(attrs={'class': 'recipe-form__description'}))
    cooking_steps = forms.CharField(max_length=10000,
                                    label="Шаги приготовления",
                                    widget=forms.Textarea(attrs={'class': 'recipe-form__cooking'}))
    cooking_time = forms.TimeField(label="Время приготовления",
                                   help_text='Укажите время приготовления',
                                   widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    image = forms.ImageField(required=False, label="Изображение блюда")
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_steps', 'cooking_time', 'image', 'meal_type')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meal_type'] = forms.ChoiceField(
            choices=[
                ('breakfast', 'Завтрак'),
                ('snack', 'Перекус'),
                ('lunch', 'Обед'),
                ('dinner', 'Ужин'),
            ],
            label="Тип приема пищи",
            widget=forms.Select(attrs={'class': 'form-control'})
        )



class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'placeholder': 'Пароль'}),
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].widget.attrs[
            'title'] = 'Минимум 8 символов. По одному из: заглавная и строчная буква, цифра и спецсимвол.'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email
class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Поиск рецептов...'
        })
    )