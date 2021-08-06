from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"sales", SaleViewSet)
router.register(r"cars", CarViewSet)
router.register(r"dealers", DealerViewSet)

urlpatterns = [
    path("", include(router.urls))
]
