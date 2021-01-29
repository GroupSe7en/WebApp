from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .models import StudentRequest

#home page of requester app
@login_required(login_url='')
def homeView(request):
    #  context = {
    #      'StudentRequests': StudentRequest.objects.all()
    #  }
    context = {}
    if request.user.groups.filter(name='Lecturer').exists():
        return render(request, 'requester/lecturerhome.html', context)#if user is a lecturer render lecturer home page
    elif request.user.groups.filter(name='Student').exists():
        return render(request, 'requester/studenthome.html', context)#if user is a lecturer render lecturer home page