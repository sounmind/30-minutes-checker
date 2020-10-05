from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from .models import Author, Tag, Action, Comment
from .forms import ActionForm
from django.urls import reverse
# Create your views here.


def index(request):
    actions = Action.objects.all().order_by('-created_time')
    context = {'page_title': "Home", 'actions': actions}
    return render(request, 'home/index.html', context)


def login(request):
    return HttpResponse('login')


def logout(request):
    return HttpResponse('logout')


def setting(request):
    return HttpResponse('setting')


def search(request):
    return HttpResponse('search')


def user(request):
    return HttpResponse('user')


def create(request):
    form = ActionForm()
    context = {'page_title': "Create Action", 'form': form}

    if request.method == "POST":
        form = ActionForm(request.POST)
        print(form)
        if form.is_valid():
            # action = form.save(commit=False)
            # 현재 사용자가 author가 되도록 처리
            # action.save()
            new_action = Action(title=form.cleaned_data['title'],
                                memo=form.cleaned_data['memo'],
                                author=form.cleaned_data['author'])
            new_action.save()
            # ManyToMany, 다중선택인 Tag 처리
            tags = form.cleaned_data['tag']
            new_action.tag.set(tags)
            print("✅ CREATE ACTION")
            return redirect("/")  # name을 사용하면 오류가 나는데 어찌된 영문?
    else:
        form = ActionForm()

    return render(request, 'home/action-create.html', context)


def edit(request, id):
    return HttpResponse('edit')


def delete(request, id):
    return HttpResponse('delete')
