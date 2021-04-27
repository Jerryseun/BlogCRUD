from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),

    ]







"""from .views import UserRegisterView
urlpatterns = [
    path('register',  UserRegisterView.as_view(), name='user_register'),

    ]
    """