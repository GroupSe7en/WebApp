from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import StudentRequest

#home page of requester app
@login_required(login_url='')
def homeView(request):
      
    if request.user.groups.filter(name='Lecturer').exists():
        context = {
          'StudentRequests': StudentRequest.objects.filter(reciever=request.user).all()
        }
        print(context)
        return render(request, 'requester/lecturerhome.html', context)#if user is a lecturer render lecturer home page
    elif request.user.groups.filter(name='Student').exists():
        context = {
          'StudentRequests': StudentRequest.objects.filter(author=request.user).all()
         }
        return render(request, 'requester/studenthome.html', context)#if user is a lecturer render lecturer home page

# class PostListView(ListView):
#     model = 