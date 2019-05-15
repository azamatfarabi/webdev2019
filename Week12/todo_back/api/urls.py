from django.urls import path
from . import views

urlpatterns = [
    path('tasklists/',views.tasklist_list),
    path('tasklists/<int:pk>/', views.tasklist_detail),
    path('tasklists/<int:pk>/tasks/', views.tasklist_tasks)
]