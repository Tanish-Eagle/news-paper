from django.urls import path

# from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]
