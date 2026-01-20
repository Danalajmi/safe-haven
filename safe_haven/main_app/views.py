from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Journal

# Create your views here.

def signup(request):
    err_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            err_msg = 'Invalid signup - please try again'
    form = UserCreationForm()
    context = {'form': form, 'err_msg': err_msg}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

class IndexJournal(ListView):
    model = Journal
    entries = Journal.objects.all()
    context_object_name = 'entries'

class CreateJournal(CreateView):
    model = Journal
    fields = '__all__'


class DetailJournal(DetailView):
    model = Journal
    context_object_name = 'entry'

class UpdateJournal(UpdateView):
    model = Journal
    fields = '__all__'

class DeleteJournal(DeleteView):
    model = Journal
    success_url = '/journals/all'
