from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import render, redirect

from user.models import User
from user.forms import UserForms


# Create your views here.

def index(request):
    users = User.objects.all()
    number_user = users.count()
    context = {
        'users': users,
        'total': number_user,
    }
    return render(request, "formUser.html", context)


def register_user(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user:register')

    form = UserForms()
    context = {
        'form': form
    }

    return render(request, 'formUser.html', context)
