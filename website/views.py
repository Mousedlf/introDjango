from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Message
from website.forms import MessageForm

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
    message = Message.objects.get(id=id)
    variables = {"message": message}
    return render(request, 'website/show.html', variables)


def delete_message(request, id):
    Message.objects.filter(id=id).delete()
    return redirect('index_messages')


def create_message(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("index_messages")

    return render(request, 'website/create.html', {"form": form})


def edit_message(request, id):
    message = Message.objects.get(id=id)
    form = MessageForm(instance=message)
    if request.method == "POST":
        form = MessageForm(data=request.POST, instance=message)
        if form.is_valid():
            message= form.save(commit=False)
            message.save()
            return redirect("show_message", message.id)
    return render(request, 'website/edit.html', {'form': form})
