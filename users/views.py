from django.shortcuts import render
from django.http import HttpResponse
from django.contrib .auth import authenticate, login

from .forms import LoginForm


def user_login(request):
    template_name = 'users/login.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleandata = form.cleaned_data
            user = authenticate(request,
                                username=cleandata['username'],
                                password=cleandata['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли')
                else:
                    return HttpResponse('Доступ запрещен')
            else:
                return HttpResponse('Ошибка входа')
        else:
            form = LoginForm()
        return render(request, template_name, {'form': form})
