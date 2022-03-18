from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from races.form import UserForm, CommentForm, RiderForm
from races.models import Rider, Race, Comment


def index(request):
    riders = Rider.objects.order_by('-created_at')[:5]
    paginator = Paginator(riders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


@login_required
def user_riders(request):
    riders = Rider.objects.filter(creator=request.user.id).order_by('-created_at')[:5]
    paginator = Paginator(riders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj, 'can_edit': True})


@login_required
def create_rider(request):
    form = RiderForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.post = form
        new_form.team_id = int(request.POST.get('team_id'))
        new_form.creator_id = request.user.id
        new_form.save()
        return HttpResponseRedirect('/riders')

    return render(request, 'rider-editor.html', {'form': form})


@login_required
def edit_rider(request, rider_id):
    return HttpResponse("You're looking for rider: %s." % rider_id)


def races(request):
    riders = Race.objects.order_by('-created_at')[:5]
    paginator = Paginator(riders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'races.html', {'page_obj': page_obj})


def race_details(request, race_id):
    race = get_object_or_404(Race, pk=race_id)

    comments = Comment.objects.filter(race=race_id).all()
    paginator = Paginator(comments, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = CommentForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.post = form
        new_form.race_id = race_id
        new_form.creator_id = request.user.id
        new_form.save()
        return HttpResponseRedirect('/races/{}'.format(race_id))

    return render(request, 'race.html', {'race': race, 'form': form, 'page_obj': page_obj})


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
