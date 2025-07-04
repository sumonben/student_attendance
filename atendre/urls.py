from django.contrib import admin
from django.urls import path,include, re_path
from . import views 
from django import views as django_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
        path('login/', views.user_login, name='login'),
        path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
        path('', views.StudentAttendanceView.as_view(), name='attendance'),
        path('get_student/', views.GetStudentView.as_view(), name='get_student'),
        path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),



]