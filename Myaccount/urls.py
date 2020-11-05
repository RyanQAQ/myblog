from django.urls import path

from .views import profile, profile_update

app_name = "Myaccount"

urlpatterns = [
    path(r'profile/', profile, name='profile'),
    path(r'profile/update/', profile_update, name='profile_update'),
]