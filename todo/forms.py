from django import forms
from .models import Todo

class TodoForm(forms.ModelForm): #사용자에서 제목,설명 등을 입력받기위해 form을 쓴다
    class Meta:
        model = Todo
        fields = ('title','description','important')