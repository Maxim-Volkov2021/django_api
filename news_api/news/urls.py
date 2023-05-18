from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
# зробити нормальні permision 👌
# додати нормальну(JWT) авторизацію
# зробити сторінку користувача
# зробити пагінацію
# зробити обробку 404 помилки