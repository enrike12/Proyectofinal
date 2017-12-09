# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import BurritosModelForm
from .models import Burritos
from .mixin import FormUserNeededMixin

# Create your views here.
def base(request):
    return render(request, "base.html")

class BurritosCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = BurritosModelForm
    template_name = "burrito/create_view.html"
    success_url = "/burritoss/list"
    login_url = "/admin"

class  BurritosUpdateView(UpdateView):
    queryset = Burritos.objects.all()
    form_class = BurritosModelForm
    template_name = "burrito/update_view.html"
    success_url = "/burritoss/list"

class BurritosDeleteView(LoginRequiredMixin, DeleteView):
    model = Burritos
    template_name = "burrito/delete_confirm.html"
    success_url = reverse_lazy("BurritoList")

class BurritosDetailView(DetailView):
    template_name = 'burrito/detail.html'
    queryset= Burritos.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Burritos.objects.get(id=id)


class BurritosListView(ListView):
        template_name = 'burrito/burrito_list.html'
        queryset= Burritos.objects.all()

        def get_queryset(self, *args, **kwargs):
            qs = Burritos.objects.all()
            print self.request.GET
            query = self.request.GET.get("q", None)
            if query is not None:
                qs = qs.filter(
                                Q(tamano__icontains=query) |
                                Q(precio__icontains=query)
                              )
            return qs

        def get_context_data(self, *args, **kwargs):
            context = super(BurritosListView, self).get_context_data(*args, **kwargs)
            print context
            context['create_form'] = BurritosModelForm()
            context['create_url'] = reverse_lazy("BurritoCreate")
            return context
