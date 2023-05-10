from rest_framework.urls import path
from . import views

urlpatterns = [
    path("order/", views.OrderView.as_view()),
    path("order/status/<int:pk>/", views.updateStatusOrderView.as_view()),
    path("order/sellers/", views.retrieveSellerOrders.as_view()),
]
