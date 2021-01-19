from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('faq/', views.portfolio, name = 'faq'),
    path('404/', views.error, name = '404'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('portfolio-single/', views.portfolio_single, name = 'portfolio-single'),
    path('services/', views.services, name = 'services'),
    path('coming_soon/', views.coming_soon, name = 'coming_soon'),
    path('pricing/', views.pricing, name = 'pricing'),
]
