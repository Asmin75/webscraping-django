from django.urls import path

from web_interface.views import QuotesListView
from . import views

app_name = 'web_interface'

urlpatterns = [
    path('', views.QuotesListView.as_view() ),
]