from django.urls import path
from allauth.account.views import LoginView, SignupView, LogoutView
from user.views import ImageView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('images/', ImageView.as_view(), name='images'),
]
