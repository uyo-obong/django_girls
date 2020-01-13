from django.shortcuts import render

from django_girls.users.forms import UserForm
from django_girls.users.models import RegisterUser


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(request.POST)
    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_user(request):
    context = {}
    return render(request, 'users/login.html', context)


def logout_user(request):
    pass
