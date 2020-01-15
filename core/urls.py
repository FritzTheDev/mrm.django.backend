from django.contrib import admin
from django.urls import path, include

from knox import views as knox_views
from .views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoginView.as_view(), name='knox_login'),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

]
