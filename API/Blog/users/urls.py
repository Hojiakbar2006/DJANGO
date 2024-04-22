from django.urls import path
from .views import SignupView, LoginView, UpdateUserProfileView, TokenRefreshExtendedView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('update_profile/', UpdateUserProfileView.as_view(),
         name='update_user_profile'),
    path('token/refresh/', TokenRefreshExtendedView.as_view(), name='token_refresh'),
]
