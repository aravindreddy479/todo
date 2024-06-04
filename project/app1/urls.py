from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.signup,name='signup'),
path('login',views.log,name='login'),
path('index/', views.index, name = 'index'),
path('add_task',views.add_task,name='add_task'),
path('view_tasks',views.view_tasks,name='view_tasks'),
 path('logout/', views.logout_view, name='logout'),
  path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),  
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'), 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)