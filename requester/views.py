from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import StudentRequest
from django.contrib.auth.mixins import LoginRequiredMixin

# #home page of requester app
# @login_required(login_url='')
# def homeView(request):
      
#     if request.user.groups.filter(name='Lecturer').exists():
#         context = {
#           'StudentRequests': StudentRequest.objects.filter(reciever=request.user).all()
#         }
#         print(context)
#         return render(request, 'requester/lecturerhome.html', context)#if user is a lecturer render lecturer home page
#     elif request.user.groups.filter(name='Student').exists():
#         context = {
#           'StudentRequests': StudentRequest.objects.filter(author=request.user).all()
#          }
#         return render(request, 'requester/studenthome.html', context)#if user is a lecturer render lecturer home page

#home page of requester app
class RequestListView(LoginRequiredMixin, ListView):

  context_object_name = 'StudentRequests'
  login_url = ''
  redirect_field_name = 'redirect_to'

  def get_queryset(self):
    if self.request.user.groups.filter(name='Lecturer').exists():
      queryset = StudentRequest.objects.filter(reciever=self.request.user).all().order_by('-date_posted')
    elif self.request.user.groups.filter(name='Student').exists():
        queryset = StudentRequest.objects.filter(author=self.request.user).all().order_by('-date_posted')
    return queryset

  def get_template_names(self):
    if self.request.user.groups.filter(name='Lecturer').exists():
      return ['requester/lecturerhome.html']
    elif self.request.user.groups.filter(name='Student').exists():
      return ['requester/studenthome.html']


class RequestDetailView(LoginRequiredMixin, DetailView):

  model = StudentRequest
  context_object_name = 'StudentRequests'
  login_url = ''
  redirect_field_name = 'redirect_to'

  def get_template_names(self):
    if self.request.user.groups.filter(name='Lecturer').exists():
      return ['requester/lecturerhome.html']
    elif self.request.user.groups.filter(name='Student').exists():
      return ['requester/studenthome.html']