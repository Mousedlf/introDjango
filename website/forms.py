from .models import Message, User, Category, Response
from django.forms import ModelForm, Textarea
from django import forms


class MessageForm(ModelForm):
     class Meta:
        model = Message
        fields = ["title", "content", "category"]
        widgets = {
            "content": Textarea(attrs={"cols": 20, "rows": 4})
        }
        category = forms.ModelChoiceField(queryset=Category.objects.all())


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ["content"]


