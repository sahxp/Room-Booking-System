from django.urls import path
from . import views 

urlpatterns = [
    path('',views.login,name='Login'),
    path('signup',views.signup,name='Sign Up'),
    path('details/<int:userId>/<str:username>/<int:productId>/',views.details,name='Details'),
    path('<int:userId>/<str:username>/',views.home,name='Home'),
    path('rooms/<int:userId>/<str:username>/',views.rooms,name='Rooms'),
    path('checkout/<int:userId>/<str:username>/<int:productId>/',views.checkout,name='Checkout'),
    path('confirmation/<int:userId>/<str:username>/<int:productId>/',views.confirmation,name='Confirmation'),
    path('subscription/<int:userId>/<str:username>/',views.subscription,name='Subscription'),
]