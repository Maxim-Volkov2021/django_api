from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

router = routers.SimpleRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/register/', RegisterApi.as_view()),

    path('api/account/profile/', AccountApi.as_view()),
]