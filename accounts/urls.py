from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name="profile"),
    path('logout/', logout_view, name="logout"),
    path('registration/', registration_view, name="registration"),
    path('basket/', basket_view, name="basket"),
    path('main/', main_view, name="main")
]