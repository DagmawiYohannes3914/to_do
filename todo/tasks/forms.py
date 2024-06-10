from django import forms
from .models import TodoItem


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"   # ['task', 'description', 'due_date', 'completed']
