from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('addreceipe',views.addreceipe, name="addreceipe"),
    path('register',views.register, name="register"),
    path('login/', views.login, name="login"),
    path('cat1',views.cat1, name="cat1"),
    path('cat2',views.cat2, name="cat2"),
    path('search', views.search, name="search"),
    path('addcatreceipe',views.addcatreceipe, name="addcatreceipe"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)