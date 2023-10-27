from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Message, User, Response
from website.forms import MessageForm, RegisterForm, ResponseForm


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
    responseForm = ResponseForm()

    return render(request, 'website/show.html', {
        "message": message,
        "responseForm": responseForm
    })


@login_required(login_url='login')
def delete_message(request, id):
    Message.objects.filter(id=id).delete()
    return redirect('index_messages')


@login_required(login_url='login')
def create_message(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect("index_messages")

    return render(request, 'website/create.html', {"form": form})


@login_required(login_url='login')
def edit_message(request, id):
    message = Message.objects.get(id=id)
    if message.author != request.user:
        return redirect('index_messages')

    form = MessageForm(instance=message)
    if request.method == "POST":
        form = MessageForm(data=request.POST, instance=message)
        if form.is_valid():
            message= form.save(commit=False)
            message.save()
            return redirect("show_message", message.id)
    return render(request, 'website/edit.html', {'form': form})


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            return redirect("login_user")

    return render(request, 'website/register.html', {"form":form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return redirect("register_user")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index_messages")

    return render(request, 'website/login.html')


def logout_user(request):
    logout(request)
    return redirect("index_messages")


def add_response(request, id):
    message = Message.objects.get(id=id)
    if message is None:
        return redirect("index_messages")
    if request.method == "POST":
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.message = message
            response.author = request.user
            response.save()

    return redirect('show_message', message.id)


def delete_response(request, id):
    response = Response.objects.get(id=id)
    Response.objects.filter(id=id).delete()
    return redirect('show_message', response.message_id)


def edit_response(request, id):
    response = Response.objects.get(id=id)
    if response.author != request.user:
        return redirect("show_message", response.message_id)

    responseForm = ResponseForm(instance=response)
    if request.method == "POST":
        responseForm = ResponseForm(data=request.POST, instance=response)
        if responseForm.is_valid():
            response = responseForm.save()
            response.save()
            return redirect("show_message", response.message_id)

    return render(request ,'website/edit_response.html', {"responseForm": responseForm})