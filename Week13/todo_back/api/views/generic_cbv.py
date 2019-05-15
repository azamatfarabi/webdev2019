from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import TaskList,Task,TaskListManager
from api.serializers import TaskListSerializer2,TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import authtoken



class TaskLists(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.all()

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer2

    def get_queryset(self):
        return TaskList.objects.all()

class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

class Tasks(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'pk2'

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        return tasklist.task_set.filter(task_list__owner=self.request.user)
