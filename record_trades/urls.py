from django.urls import path

from . import views

urlpatterns = [
    path('add_trade', views.CreateNewTradeView.as_view(), name='add_trade'),
    path('get_all_trades', views.GetAllTradesView.as_view(), name='get_all_trades'),
]
