from django.urls import path
from . import views



app_name = 'mains'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('faq/', views.faq, name = 'faq'),
    path('404/', views.error, name = '404'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('portfolio_single/', views.portfolio_single, name = 'portfolio_single'),
    path('services/', views.services, name = 'services'),
    path('coming_soon/', views.coming_soon, name = 'coming_soon'),
    path('pricing/', views.pricing, name = 'pricing'),
]
