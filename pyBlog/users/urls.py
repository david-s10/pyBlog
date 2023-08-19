from django.urls import path

from .views import CustomRegisterView, CustomLogoutView, CustomLoginView, UserProfile


urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', UserProfile.as_view(), name='user-profile')
]

