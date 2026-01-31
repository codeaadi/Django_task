from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, task_list, task_create, task_update,task_update

urlpatterns = [
    path('',task_list,name='task_list'),
     path('create/', task_create, name='task_create'),
    path('login/',auth_views.LoginView.as_view(template_name='tasks/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(next_page='login'),name='logout'),
    path('signup/',signup,name='signup'),
  path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/',task_update, name='task_delete'),
]
