from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import StudentRequest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

  def get_template_names(self):
    if self.request.user.groups.filter(name='Lecturer').exists():
      return ['requester/lecturer_requestdetail.html']
    elif self.request.user.groups.filter(name='Student').exists():
      return ['requester/student_requestdetail.html']


class RequestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

  model = StudentRequest
  fields = ['requestType', 'title', 'content', 'reciever']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    if (self.request.user.groups.filter(name='Student').exists()):
      return True
    return False


class RequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

  model = StudentRequest
  fields = ['requestType', 'title', 'content', 'reciever']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    request = self.get_object()
    if (self.request.user == request.author):
      return True
    return False


class RequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

  model = StudentRequest
  success_url = "/requester/home/"

  def test_func(self):
    request = self.get_object()
    if (self.request.user == request.author):
      return True
    return False


class RequestReviewView(LoginRequiredMixin, UserPassesTestMixin, View):

  def test_func(self):
    studentrequest = StudentRequest.objects.filter(id = self.kwargs['pk']).first()
    if (self.request.user == studentrequest.reciever):
      if (self.kwargs['review'] == 'accept'):
        studentrequest.accept_status = 'AC'
        studentrequest.save()
      elif (self.kwargs['review'] == 'reject'):
        studentrequest.accept_status = 'RJ'
        studentrequest.save()
      return True
    return False

  def get(self, request, *args, **kwargs):
        return redirect('request-detail', pk = kwargs['pk'])
