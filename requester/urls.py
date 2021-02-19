from django.urls import path
from . import views
from .views import RequestListView, RequestDetailView

urlpatterns = [
    path('home/', RequestListView.as_view(), name='requester-home'),#url to home page
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),#dynamic url to request detail page
]