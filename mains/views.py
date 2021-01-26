from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request, 'mains/index.html')

    # Create your views here.
def portfolio(request):
    
    return render(request, 'mains/portfolio.html')

def faq(request):
    return render(request, 'mains/faq.html')

def error(request):
    return render(request, 'mains/404.html')


def contact(request):
    return render(request, 'mains/contact.html')


def about(request):
    return render(request, 'mains/about.html')

def portfolio_single(request):
    return render(request, 'mains/portfolio_single.html')

def coming_soon(request):
    return render(request, 'mains/coming_soon.html')
def pricing(request):
    return render(request, 'mains/pricing.html')
def services(request):
    return render(request, 'mains/services.html')