from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

    # Create your views here.
def portfolio(request):
    return render(request, 'main/portfolio.html')

def faq(request):
    return render(request, 'main/faq.html')

def error(request):
    return render(request, 'main/404.html')


def contact(request):
    return render(request, 'main/contact.html')


def about(request):
    return render(request, 'main/about.html')

def portfolio_single(request):
    return render(request, 'main/portfolio-single.html')

def coming_soon(request):
    return render(request, 'main/coming_soon.html')
def pricing(request):
    return render(request, 'main/pricing.html')
def services(request):
    return render(request, 'main/services.html')