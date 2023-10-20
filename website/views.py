from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.


def index(request):
    variables = {
        "message": "coucou"
    }
    return render(request, 'website/home.html', variables)


def noot(request):
    variables = {"message": "t moche"}
    return render(request, 'website/noot.html', variables)


def index_messages(request):
    messages = Message.objects.all()
    variables = {"messages": messages}
    return render(request, 'website/messages.html', variables)


def show_message(request, id):
    message = Message.objects.get(id= id)
    variables = {"message": message}
    return render(request, 'website/show.html', variables)
