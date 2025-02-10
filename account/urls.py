from django.urls import path
from .views import signUp, disconnect_user, login_user


urlpatterns = [

    path('signUp/', signUp, name='signUp'),
    path('login_user/', login_user, name='login_user'),
    path('disconnect/', disconnect_user, name='disconnect_user'),
]