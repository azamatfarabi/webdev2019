from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import TaskList


def tasklist_list(request):
    task_lists = TaskList.objects.all()
    json_tasklists = [t.to_json() for t in task_lists]
    return JsonResponse(json_tasklists, safe=False)

def tasklist_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist.to_json())

def tasklist_tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasklist.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks,safe=False)