from django.urls import path
from . import views 

urlpatterns = [
    path('login/',views.login,name='Login'),
    path('<int:userId>/<str:username>/',views.home,name='Home'),
    path('listing-stay/',views.listing_stay,name='Listing Stay'),
]