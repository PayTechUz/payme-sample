from django.urls import path

from apps.shop.views.buy import buy_view
from apps.shop.views.home import home_view
from apps.shop.views.pay_link import GeneratePayLinkAPIView


urlpatterns = [
    path('', home_view, name='home'),
    path('<str:pk>/buy/', buy_view, name='buy'),
    path('pay-link/', GeneratePayLinkAPIView.as_view(), name='generate-pay-link')
]
