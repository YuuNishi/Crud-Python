from django.shortcuts import render, redirect
from app.forms import ProfileForms
from app.models import Profile


# Create your views here.
def home(request):
    data = {}
    data['dbs'] = Profile.objects.all()
    data['form'] = ProfileForms
    data['action'] = 'Cadastrar'
    return render(request, 'Index.html', data)


def create(request):
    forms = ProfileForms(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('home')


def modify(request, pk):
    data = {}
    data['db'] = Profile.objects.get(pk=pk)
    data['form'] = ProfileForms(instance=data['db'])
    data['dbs'] = Profile.objects.all()
    data['action'] = 'Editar'
    return render(request, 'Index.html', data)


def update(request, pk):
    data = {}
    data['db'] = Profile.objects.get(pk=pk)
    forms = ProfileForms(request.POST or None, instance=data['db'])
    if forms.is_valid():
        forms.save()
        return redirect('home')


def delete(request, pk):
    db = Profile.objects.get(pk=pk)
    db.delete()
    return redirect('home')
