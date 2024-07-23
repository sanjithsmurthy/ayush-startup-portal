from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('adminn/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('accounts/', include('allauth.urls')),
    
]
