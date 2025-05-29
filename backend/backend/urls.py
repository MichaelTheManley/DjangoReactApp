from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentication
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api-auth/', include('rest_framework.urls')),
    # API resources
    path('api/', include('api.urls')) # Include the API URLs for notes and other resources that aren't listed above
]
