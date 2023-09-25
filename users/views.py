from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from realty.models import Realty
from users.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from users.models import Profile, Subscriber, Favorites

import time

import threading

def index_views(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    # delete entry from favorites
    if 'action' in request.GET and request.GET['action'] == 'delete_from_favorites':
        favorite_id = request.GET['id']
        entry = Favorites.objects.filter(id=favorite_id)
        entry.delete()

    user = request.user
    favorites = Favorites.objects.filter(user=user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'favorites': favorites})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


# def user_login_old(request):
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Authenticated successfully')
#
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#
#     else:
#         form = LoginForm()
#
#     return render(request, 'login.html', {'form': form})

