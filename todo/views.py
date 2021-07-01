from django.views.generic.edit import UpdateView
from todo.models import Todomodel
from django.db import models
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = "list.html"
    model = Todomodel


class TodoDetail(DetailView):
    template_name = "detail.html"
    model = Todomodel


class TodoCreate(CreateView):
    template_name = "create.html"
    model = Todomodel
    fields = ("title", "memo", "priority", "duedate")
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = Todomodel
    success_url = reverse_lazy("list")


class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = Todomodel
    fields = ("title", "memo", "priority", "duedate")
    success_url = reverse_lazy("list")
