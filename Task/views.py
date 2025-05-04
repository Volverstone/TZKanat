from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# @method_decorator(login_required, name='dispatch')
# class TaskListView(ListView):
#     model = Task



from django.views.generic import ListView
from .models import Task
from django.db.models import Q

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/view_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()


        status = self.request.GET.get('status')
        if status == 'done':
            queryset = queryset.filter(status=True)
        elif status == 'pending':
            queryset = queryset.filter(status=False)

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        sort = self.request.GET.get('sort')
        if sort == 'date':
            queryset = queryset.order_by('-created_at')  # Сначала новые
        elif sort == 'status':
            queryset = queryset.order_by('status')  # Сначала "в процессе"
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', '')
        context['search_query'] = self.request.GET.get('q', '')
        context['sort_option'] = self.request.GET.get('sort', '')
        return context

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'tasks/view_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'tasks/view_create.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('task_list')


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'tasks/view_update.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('task_list')
