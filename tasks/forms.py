from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'autocomplete': 'username',
        }),
        help_text='Use até 150 caracteres. Letras, números e @/./+/-/_.',
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'new-password',
        }),
        help_text='',
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repita a senha',
            'autocomplete': 'new-password',
        }),
        help_text='',
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Tarefa',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descreva a tarefa...',
            'autofocus': True,
        }),
    )
    priority = forms.ChoiceField(
        label='Prioridade',
        choices=Task.Priority.choices,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    deadline = forms.DateField(
        label='Data limite',
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
    )

    class Meta:
        model = Task
        fields = ['title', 'priority', 'deadline']
