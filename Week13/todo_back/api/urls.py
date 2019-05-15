from django.urls import path
from api import views


# urlpatterns = [
#     path('tasklists/',views.tasklist_list),
#     path('tasklists/<int:pk>/', views.tasklist_detail),
#     path('tasklists/<int:pk>/tasks/', views.tasklist_tasks)
# ]

urlpatterns = [
    path('tasklists/',views.TaskLists.as_view()),
    path('tasklists/<int:pk>/', views.TaskListDetail.as_view()),
    path('tasklists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)

    # path('tasklists/<int:pk>/tasks/<int:pk2>/', views.Tasks.as_view())
]

