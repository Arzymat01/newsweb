from django.shortcuts import render, HttpResponse
from .models import Newsweb

# Create your views here.


def index(request):
    news = Newsweb.objects.all()

    context = {
        'newsbest': news,
    }
    return render(request, ('newsWebsite/index.html', context))


def business(request):
    news = Newsweb.objects.all()

    context = {
        "news": news,
    }
    return render(request, ('newsWebsite/business.html', context))


def health(request):
    return render(request, ('newsWebsite/health.html'))


def politika(request):
    return render(request, ('newsWebsite/politika.html'))


def sport(request):
    return render(request, ('newsWebsite/sport.html'))


def technology(request):
    return render(request, ('newsWebsite/technology.html'))
