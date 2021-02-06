from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='')
def profile(request):
    if request.user.groups.filter(name='Lecturer').exists():
        return render(request, 'users/lecturerprofile.html')#if user is a lecturer render lecturer profile page
    elif request.user.groups.filter(name='Student').exists():
        return render(request, 'users/studentprofile.html')#if user is a lecturer render lecturer profile page
