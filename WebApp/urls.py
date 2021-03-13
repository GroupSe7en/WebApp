from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from requester.views import RequestListView
import notifications.urls

urlpatterns = [
    path('logout/', user_views.logout_user, name='logout'),#logout view route
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('requester/', include('requester.urls')),#adding requester app url config
    path('', RequestListView.as_view(), name='requester-home'),#url to home page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#login view route
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
        name='password_reset'),#password reset route
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),#logout view route
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),  
        name='password_reset_confirm'),#password reset confirm view route
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),#password reset complete route
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'), 
        name='password_change'),#password change route
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), 
        name='password_change_done'),#password change done route
    path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
