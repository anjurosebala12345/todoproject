from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForm

from django.views.generic import ListView, UpdateView, DeleteView
from .models import Task
from django.views.generic.detail import DetailView


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_list'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url= reverse_lazy('cbv')


def add(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        data = Task(name=task, priority=priority, date=date)
        data.save()
    return render(request, "home.html", {'task_list': task_list})


def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


# def details(request):
#     task = Task.objects.all()
#     return render(request, "details.html",{'task':task})


def edit(request, id):
    task = Task.objects.get(id=id)
    a = TodoForm(request.POST or None, instance=task)
    if a.is_valid():
        a.save()
        return redirect('/')
    return render(request, 'edit.html', {'a': a, 'task': task})
