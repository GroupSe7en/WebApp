from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import StudentProfileUpdateForm, LecturerProfileUpdateForm
from notifications.signals import notify
from django.views.generic import TemplateView

@login_required(login_url='login/')
def profile(request):
    if request.user.groups.filter(name='Lecturer').exists():

        if request.method == 'POST':
            lp_form = LecturerProfileUpdateForm(request.POST, request.FILES, instance=request.user.lecturerprofile)
            if lp_form.is_valid():
                lp_form.save()
                messages.success(request, f'Your profile has been updated')
                return redirect('profile')
        else:
            lp_form = LecturerProfileUpdateForm(instance=request.user.lecturerprofile)

        context = {
            'lp_form': lp_form
        }

        return render(request, 'users/lecturerprofile.html', context)

    elif request.user.groups.filter(name='Student').exists():

        if request.method == 'POST':
            sp_form = StudentProfileUpdateForm(request.POST, request.FILES, instance=request.user.studentprofile)
            if sp_form.is_valid():
                sp_form.save()
                messages.success(request, f'Your profile has been updated')
                return redirect('profile')
        else:
            sp_form = StudentProfileUpdateForm(instance=request.user.studentprofile)

        context = {
            'sp_form': sp_form
        }

        return render(request, 'users/studentprofile.html', context)

@login_required(login_url='login/')
def logout_user(request):
    qs = request.user.notifications.unread()
    qs.mark_all_as_read()
    logout(request)
    return render(request, 'users/logout.html')

class HelpView(TemplateView):
    template_name = "users/help.html"

class AboutView(TemplateView):
    template_name = "users/contact.html"
