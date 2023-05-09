from rest_framework.urls import path
from . import views

urlpatterns = [path("order/", views.OrderView.as_view())]
