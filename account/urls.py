
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
path('',views.dashboard,name='dashboard'),
path('signup/',views.signup,name='signup'),
path('login/',views.login_view,name='login'),
path('logout/',views.logoutUser,name='logout'),
path('profile/',views.profile_settings,name='profile')
]
