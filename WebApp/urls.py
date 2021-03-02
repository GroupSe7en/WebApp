from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from requester.views import RequestListView

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),#logout view route
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('requester/', include('requester.urls')),#adding requester app url config
    path('', RequestListView.as_view(), name='requester-home'),#url to home page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login')#login view route
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
