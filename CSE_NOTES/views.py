from django.shortcuts import render
from django.http import HttpResponse
from .models import cnscl, cg, ss, opr, os,pyth


# Create your views here.
def index(request):
    return render(request, "index.html")


def cryptography(request):
    anss = cnscl.objects.all().order_by('qno')
    return render(request, "index.html", {'anss': anss})


def computergraphics(request):
    anss = cg.objects.all()
    return render(request, "index.html", {'anss': anss})


def systemsofware(request):
    anss = ss.objects.all().order_by('qno')
    return render(request, "index.html", {'anss': anss})


def operatingsystem(request):
    anss = os.objects.all().order_by('qno')
    return render(request, "index.html", {'anss': anss})


def operationalresearch(request):
    anss = opr.objects.all().order_by('qno')
    return render(request, "index.html", {'anss': anss})


def python(request):
    anss = pyth.objects.all().order_by('qno')
    return render(request, "index.html", {'anss': anss})
