from django.shortcuts import render, redirect
from django.contrib import messages
from .models import show


def Shows(request):
    context = {
        "All_Shows": show.objects.all()
    }

    return render(request, 'shows.html', context)

def AddShow(request):
    return render(request, 'newshow.html')


def CreateShow(request):
    Title_post = request.POST['title']
    Network_post = request.POST['network']
    ReleaseDate_post = request.POST['release_date']
    Description_post = request.POST['description']
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        show.objects.create(Title=Title_post, Network=Network_post, Release_date=ReleaseDate_post, Description=Description_post)
        return redirect('/')
def ShowShow(request, idshow):
    TVShow = show.objects.get(id= idshow)

    context = {
        'TvShow': TVShow
    }
    return render(request, 'TVshow.html', context)
def ShowEdit(request, idshow):
    context = {
        'EditShow': show.objects.get(id= idshow)
    }
    return render(request, 'edit.html', context)

def ShowUpdate(request, idshow):
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/idshow/edit')
    else:
        c = show.objects.get(id=idshow)
        c.Title = request.POST['title']
        c.Network = request.POST['network']
        c.Release_date = request.POST['release_date']
        c.Description = request.POST['description']
        c.save()
        return redirect('/')

def deleteShow(request, idshow):
    x = show.objects.get(id= idshow)
    x.delete()
    return redirect('/')
# Create your views here.
