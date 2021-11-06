from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from UserApp.forms import SignUpForm, UserForm, ProfileForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    return render(request, 'register.html')


def delete(request):

    if request.method == 'POST':
        id = request.user.id
        user = User.objects.filter(id=id)
        user.delete()
        return redirect('home')


    return render(request, 'delete.html')


def update(request):
    id = request.user.id
    p = Profile.objects.filter(id=id)
    return render(request, 'settings.html', {'p': p})


def profdis(request):
    id = request.user.id
    p = Profile.objects.filter(id=id)
    return render(request, 'profdis.html', {'p': p})


# @login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('update')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.job = form.cleaned_data.get('job')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.img = form.cleaned_data.get('img')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
