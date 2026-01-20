from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Journal, Article

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
    articles = Article.objects.all()
    entries = Journal.objects.all()
    return render(request, 'home.html', {'articles': articles, 'entries': entries})

class IndexJournal(ListView):
    model = Journal
    #! change to .filter after applying auth
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

class IndexArt(ListView):
    model = Article
    articles = Article.objects.all()
    context_object_name = 'articles'

class CreateArt(CreateView):
    model = Article
    fields = '__all__'

class UpdateArt(UpdateView):
    model = Article
    fields = '__all__'

class DetailArt(DetailView):
    model = Article
    context_object_name = 'article'

class DeleteArt(DeleteView):
    model = Article
    success_url = '/'

