from django.urls import path
from . import views 

urlpatterns = [
    path('',views.login,name='Login'),
    path('signup',views.signup,name='Sign Up'),
    path('<int:userId>/<str:username>/',views.home,name='Home'),
    path('listing-stay/',views.listing_stay,name='Listing Stay'),
]