from django.urls import path
from . import views
from .views import RequestListView, RequestDetailView, RequestCreateView, RequestUpdateView, RequestDeleteView

urlpatterns = [
    path('home/', RequestListView.as_view(), name='requester-home'),#url to home page
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),#dynamic url to request detail page
    path('request/new/', RequestCreateView.as_view(), name='request-create'),#url to request create page
    path('request/<int:pk>/update/', RequestUpdateView.as_view(), name='request-update'),#dynamic url to request update page
     path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request-delete'),#dynamic url to request update page
]
