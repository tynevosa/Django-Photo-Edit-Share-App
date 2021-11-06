from django.shortcuts import render, redirect
import datetime
from PhotoApp.models import Photo, Posts
from django.contrib.auth.models import User
from .forms import Photoforms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'index.html')


@login_required()
def cat(request, key):
    obj = Photo.objects.filter(Category=key, Visibility='Public').exclude(Owner_id=request.user).order_by('-Date')

    paginator = Paginator(obj, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pg = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pg = paginator.page(paginator)

    return render(request, 'allphoto.html', {'obj': obj, 'ct': cat, 'pg': pg})

    # return render(request, 'allphoto.html', {'obj': obj})


@login_required()
def hat(request, key):
    obj = Photo.objects.filter(Owner_id=request.user, Category=key).order_by('-Date')

    paginator = Paginator(obj, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pg = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pg = paginator.page(paginator)

    return render(request, 'aphoto.html', {'obj': obj, 'ct': cat, 'pg': pg})
    # return render(request, 'aphoto.html', {'obj': obj})


def dphoto(request, id):
    poto = Photo.objects.filter(id=id)
    post = Posts.objects.filter(Photoid=id)

    if request.method == "POST":
        Comment = request.POST.get('Comment')
        on = request.user
        obj = Posts(Comment=Comment, Photoid_id=id, By=on)
        obj.save()

    return render(request, 'dphoto.html', {'poto': poto, 'post': post})


@login_required()
def photo(request):
    obj = Photo.objects.filter(Owner_id=request.user).order_by('-Date')

    paginator = Paginator(obj, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pg = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pg = paginator.page(paginator)

    return render(request, 'aphoto.html', {'obj': obj, 'ct': cat, 'pg': pg})

    # return render(request, 'aphoto.html', {'obj': obj})


@login_required()
def allphoto(request):
    obj = Photo.objects.filter(Visibility='Public').exclude(Owner_id=request.user).order_by('-Date')

    paginator = Paginator(obj, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pg = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pg = paginator.page(paginator)

    return render(request, 'allphoto.html', {'obj': obj, 'ct': cat, 'pg': pg})
    # return render(request, 'allphoto.html', {'obj': obj})


@login_required()
def addphoto(request):
    if request.method == 'POST':
        form = Photoforms(request.POST, request.FILES)
        if form.is_valid():
            obj = Photo()
            # p.refresh_from_db()  # load the profile instance created by the signal
            obj.Title = form.cleaned_data.get('Title')
            obj.Location = form.cleaned_data.get('Location')
            obj.Category = form.cleaned_data.get('Category')
            obj.Image = form.cleaned_data.get('Image')
            obj.Description = form.cleaned_data.get('Description')
            obj.Visibility = form.cleaned_data.get('Visibility')
            uid = request.user.id
            user = User.objects.get(id=uid)
            obj.Owner = user
            obj.Date = datetime.datetime.now()
            obj.save()

            return redirect('photo')
    else:
        form = Photoforms()
    return render(request, 'addphoto.html', {'form': form})


def delete(request, id):
    poto = Photo.objects.get(id=id)
    if request.method == 'POST':
        poto.delete()
        return redirect('photo')

    return render(request, 'delete.html', {'poto': poto})


def update(request, id):
    poto = Photo.objects.get(id=id)
    if request.method != 'POST':
        form = Photoforms(instance=poto)
    else:
        form = Photoforms(data=request.POST, files=request.FILES, instance=poto)
        if form.is_valid():
            form.save()
            return redirect('photo')

    return render(request, 'edit.html', {'poto': poto, 'form': form})


@login_required()
def searching(request):
    prod = None
    qy = None
    if 'q' in request.GET:
        qy = request.GET.get('q')
        prod = Photo.objects.all().filter(
            Q(Title__icontains=qy) | Q(Description__icontains=qy) | Q(Location__icontains=qy) | Q(Category__icontains=qy))

    return render(request, 'search.html', {'qr': qy, 'pr': prod})


@login_required()
def search(request):
    return render(request, 'search.html')
