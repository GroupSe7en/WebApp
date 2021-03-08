from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import StudentRequest, Comment, CommentReply
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import django_filters 

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
# class RequestListView(LoginRequiredMixin, ListView):

#   context_object_name = 'StudentRequests'

#   def get_queryset(self):
#     if self.request.user.groups.filter(name='Lecturer').exists():
#       queryset = StudentRequest.objects.filter(reciever=self.request.user).all().order_by('-date_posted')
#     elif self.request.user.groups.filter(name='Student').exists():
#         queryset = StudentRequest.objects.filter(author=self.request.user).all().order_by('-date_posted')
#     return queryset

#   def get_template_names(self):
#     if self.request.user.groups.filter(name='Lecturer').exists():
#       return ['requester/lecturerhome.html']
#     elif self.request.user.groups.filter(name='Student').exists():
#       return ['requester/studenthome.html']

#######################################################################################################################################

class StudentRequestFilterset(django_filters.FilterSet):
    class Meta:
        model = StudentRequest
        fields = {
            'requestType': ['exact'],
            'reciever__email': ['exact', 'contains'],
            'requestType': ['exact'],
            'title' : ['contains'],
            'date_posted' : ['exact'],
            'accept_status' : ['exact'],
        }
  
class LecturerRequestFilterset(django_filters.FilterSet):
  class Meta:
      model = StudentRequest
      fields = {
          'requestType': ['exact'],
          'author__email': ['exact', 'contains'],
          'requestType': ['exact'],
          'title' : ['contains'],
          'date_posted' : ['exact'],
          'accept_status' : ['exact'],
      }

class RequestListView(ListView):
    filterset_class = None

    def get_queryset(self):
      if self.request.user.groups.filter(name='Lecturer').exists():
        queryset = StudentRequest.objects.filter(reciever=self.request.user).all().order_by('-date_posted')
        self.filterset_class = LecturerRequestFilterset
      elif self.request.user.groups.filter(name='Student').exists():
        queryset = StudentRequest.objects.filter(author=self.request.user).all().order_by('-date_posted')
        self.filterset_class = StudentRequestFilterset
      # Then use the query parameters and the queryset to
      # instantiate a filterset and save it as an attribute
      # on the view instance for later.
      self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
      # Return the filtered queryset
      return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context
    

    def get_template_names(self):
      if self.request.user.groups.filter(name='Lecturer').exists():
        return ['requester/lecturerhome.html']
      elif self.request.user.groups.filter(name='Student').exists():
        return ['requester/studenthome.html']

#################################################################################################################

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
    if ((self.request.user == request.author) and (StudentRequest.objects.filter(id = self.kwargs['pk']).first().accept_status == 'PN')):
      return True
    return False


class RequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

  model = StudentRequest
  success_url = ""

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


class AddCommentView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

  model = Comment
  fields = ['body']

  def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.studentrequest = StudentRequest.objects.filter(id = self.kwargs['pk']).first()
    return super().form_valid(form)
  
  def test_func(self):
    studentrequest = StudentRequest.objects.filter(id = self.kwargs['pk']).first()
    if (self.request.user == studentrequest.author) or (self.request.user == studentrequest.reciever):
      return True
    return False


class AddReplyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

  model = CommentReply
  fields = ['body']

  def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.comment = Comment.objects.filter(id = self.kwargs['commentpk']).first()
    return super().form_valid(form)
  
  def test_func(self):
    comment = Comment.objects.filter(id = self.kwargs['commentpk']).first()
    if (self.request.user == comment.studentrequest.author) or (self.request.user == comment.studentrequest.reciever):
      return True
    return False