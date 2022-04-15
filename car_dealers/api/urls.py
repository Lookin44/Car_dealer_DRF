from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CarViewSets, DealerViewSets

router = SimpleRouter()
router.register(r'dealers', DealerViewSets)
router.register(r'cars', CarViewSets)

urlpatterns = [
    path('v1/', include(router.urls)),
]
