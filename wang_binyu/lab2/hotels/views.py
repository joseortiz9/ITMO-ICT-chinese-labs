from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from hotels.form import UserForm


def index(request):
    return render(request, 'home.html')


def hotels(request):
    return render(request, 'hotels.html')


def hotel_details(request, hotel_id):
    return render(request, 'hotel.html')


def user_rooms(request):
    return render(request, 'rooms.html')


def room_details(request, room_id):
    return render(request, 'room.html')


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'error_msg': "Incorrect username or password"})
    else:
        return render(request, 'login.html', {})


def user_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    registered = False
    if request.method == 'POST':
        create_user_form = UserForm(data=request.POST)
        if create_user_form.is_valid():
            user = create_user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print(create_user_form.errors)
    else:
        create_user_form = UserForm()

    return render(request, 'register.html', {'create_user_form': create_user_form, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')