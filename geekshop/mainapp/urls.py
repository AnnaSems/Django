from django.urls import path, include
from .views import main, products, contact

urlpatterns = [
    path('', main, name='index'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth'))
]
