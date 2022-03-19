from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from hotels.form import UserForm
from hotels.models import Hotel, Room


def index(request):
    return render(request, 'home.html')


def hotels(request):
    hotels_set = Hotel.objects.order_by('-created_at')[:5]
    paginator = Paginator(hotels_set, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'hotels.html', {'page_obj': page_obj})


@login_required
def hotel_details(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    rooms = Room.objects.filter(hotel=hotel_id).order_by('-created_at')[:5]
    paginator = Paginator(rooms, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hotel.html', {'hotel': hotel, 'page_obj': page_obj})


@login_required
def reserve_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if room.guests.count() > 0:
        return HttpResponse('This room is busy :( try with other one!')
    else:
        room.guests.add(request.user)
        return HttpResponseRedirect('/rooms')


@login_required
def user_rooms(request):
    rooms = Room.objects.filter(guests__in=[request.user.id]).order_by('-created_at')[:5]
    paginator = Paginator(rooms, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'rooms.html', {'page_obj': page_obj})


@login_required
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