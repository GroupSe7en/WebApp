from django.urls import path
from . import views
from .views import (
    RequestListView,
    RequestDetailView,
    RequestCreateView,
    RequestUpdateView,
    RequestDeleteView,
    RequestReviewView,
    AddCommentView,
    AddReplyView)

urlpatterns = [
    path('home/', RequestListView.as_view(), name='requester-home'),#url to home page
    path('request/new/', RequestCreateView.as_view(), name='request-create'),#url to request create page
    path('request/<int:pk>/update/', RequestUpdateView.as_view(), name='request-update'),# url to request update page
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request-delete'),# url to request update page
    path('request/<int:pk>/review/<str:review>/', RequestReviewView.as_view(), name='request-review'),# url to request review
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),# url to request detail page
    path('request/<int:pk>/addcomment/', AddCommentView.as_view(), name='request-addcomment'),# url to add comment page
    path('request/<int:pk>/comment<int:commentpk>/replycomment/', AddReplyView.as_view(), name='request-replycomment'),#url to reply comment page

]
