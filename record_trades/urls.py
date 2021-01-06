from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_trade', views.CreateNewTradeView.as_view(), name='add_trade'),
    path('view_trades/status=<status>', views.GetAllTradesView.as_view(), name='view_filtered_trades'),
]
