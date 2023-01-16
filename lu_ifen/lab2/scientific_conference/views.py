from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .form import *
from .models import *


@csrf_exempt
def user_login(request):


    if request.method == 'POST':
        if request.POST.get('username') == None:
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('http://127.0.0.1:8000/conferences/'+str(user.id))

            else:
                return render(request, 'login.html', {'error_msg': "Incorrect username or password"})
    else:
        return render(request, 'login.html')


def user_register(request):

    registered = False
    if request.method == 'POST':
        create_user_form = User_form(data=request.POST)
        if create_user_form.is_valid():
            user = create_user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('http://127.0.0.1:8000/conferences/'+str(user.id))
        else:
            print(create_user_form.errors)
    else:
        create_user_form = User_form()

    return render(request, 'register.html', {'create_user_form': create_user_form, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def list_conferences(request, user_id):
    id = user_id
    conferences = Conference.objects.order_by('-date')[:5]
    return render(request, 'conferences.html', {'list': conferences, 'user': id})

@login_required
def list_Presentation(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    list_user = []
    Presentations = list(Presentation.objects.filter(conference=conference_id).all())
    for i in Presentations:
        authors = User.objects.get(id=i.author.id)
        list_user.append(authors)
    print(list_user)
    return render(request, 'authors.html', {'list': list_user,'conference': conference})

@login_required
def create_presentation(request,conference_id,user_id):
    user = get_object_or_404(User, pk=user_id)
    conference = get_object_or_404(Conference, pk=conference_id)
    new_presentation = Presentation()
    new_presentation.author = user
    new_presentation.conference = conference
    new_presentation.save()

    return HttpResponseRedirect('http://127.0.0.1:8000/authors/'+str(conference.id))

@login_required
def list_review(request, user_id,conference_id):
    id = user_id
    conference = get_object_or_404(Conference, pk=conference_id)
    review = Review.objects.filter(conference=conference_id).all()
    return render(request, 'reviews.html', {'list': review, 'user': id, 'conference':conference})

@login_required
def create_review(request,user_id,conference_id):
    user = get_object_or_404(User, pk=user_id)
    conference = get_object_or_404(Conference, pk=conference_id)
    new_review = Review()
    new_review.text = request.POST.get('text')
    new_review.conference = conference
    new_review.rating = request.POST.get('rating')
    new_review.creator = user
    new_review.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/review/'+str(user.id)+'/'+str(conference.id))

@login_required
def list_my_conference(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    list_conference = []

    conferences = list(Presentation.objects.filter(author=user.id).all())

    for i in conferences:
        my_conference = Conference.objects.get(id=i.conference.id)
        list_conference.append(my_conference)
    print(list_conference)
    return render(request, 'my_conference.html', {'list': list_conference, 'user': user})

@login_required
def presentation_edit(request,user_id,conference_id):
    user = get_object_or_404(User, pk=user_id)
    conference = get_object_or_404(Conference, pk=conference_id)
    
    presentation = Presentation.objects.filter(conference=conference.id,author = user.id).first()
    presentation.delete()

    return HttpResponseRedirect('http://127.0.0.1:8000/my_conference/'+str(user.id))