
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from api.views import ImportView   
from django.contrib.auth import authenticate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^import/', ImportView.as_view(), name='import'),
    url(r'^api/', include('api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]

