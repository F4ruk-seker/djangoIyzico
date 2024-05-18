from django.urls import path, include
from payment.api.views import Payment, ResultView


urlpatterns: list[path] = [
    path('payment', Payment.as_view()),
    path('result', ResultView.as_view()),
]
