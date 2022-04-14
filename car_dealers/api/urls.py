from django.urls import path

from .views import *

urlpatterns = [
    path('dealer/create/', DealerCreateView.as_view()),
    path('dealer/', DealerListView.as_view()),
    path('dealer/<int:pk>/', DealerDetailView.as_view()),
    path('dealer/<int:pk>/destroy/', DealerDestroyView.as_view()),
    path('car/coming/', CarCreateView.as_view()),
    path('car/', CarListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/<int:pk>/sell/', CarSellView.as_view()),
]
