
from django.urls import path

from accounts.views import logout_view, RegistrationView, LoginView, ProfileView, CretePost, UserChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('post/', CretePost.as_view(), name='post'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
]