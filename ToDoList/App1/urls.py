from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
path('',views.login_page,name='login_page'),
path('register-page/',views.register_page,name='register_page'),
path('login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
path('register/',views.register,name='register'),
path('dashboard/',views.dashboard,name='dashboard'),
path('add-task/',views.add_task,name='add_task'),
path('edit-task/<int:task_id>/',views.edit_task,name='edit_task'),
path('delete-task/<int:task_id>/',views.delete_task,name='delete_task'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)