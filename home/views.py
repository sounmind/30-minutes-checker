from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from .models import Author, Tag, Action, Comment
from .forms import ActionForm, TagForm
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


def action_create(request):
    # form = ActionForm() # 없어도 되나?

    if request.method == "POST":
        form = ActionForm(request.POST)
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
    context = {'page_title': "Create Action", 'form': form}
    return render(request, 'home/action-create-edit.html', context)


def action_edit(request, id):
    action = get_object_or_404(Action, pk=id)
    if request.method == "POST":
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            new_action = Action(title=form.cleaned_data['title'],
                                memo=form.cleaned_data['memo'],
                                author=form.cleaned_data['author'])
            new_action.save()
            tags = form.cleaned_data['tag']
            new_action.tag.set(tags)
            print("✅ EDIT ACTION")
            return redirect("/")  # name을 사용하면 오류가 나는데 어찌된 영문?
    else:
        form = ActionForm(instance=action)
    context = {'page_title': "Edit Action", 'form': form}
    return render(request, 'home/action-create-edit.html', context)


def action_delete(request, id):
    action = Action.objects.get(id=id)
    action.delete()
    return redirect('/')


def tag_view(request):
    tags = Tag.objects.all().order_by('title')
    context = {'page_title': "Tag", 'tags': tags}
    return render(request, 'home/tag-view.html', context)


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = Tag(title=form.cleaned_data['title'])
            new_tag.save()
            print("✅ CREATE TAG")
            return redirect("/")  # name을 사용하면 오류가 나는데 어찌된 영문?
    else:
        form = TagForm()
    context = {'page_title': "Create Tag", 'form': form}
    return render(request, 'home/tag-create-edit.html', context)


def tag_edit(request, id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            new_tag = Tag(title=form.cleaned_data['title'])
            new_tag.save()
            print("✅ EDIT TAG")
            return redirect("/")  # name을 사용하면 오류가 나는데 어찌된 영문?
    else:
        form = TagForm(instance=tag)
    context = {'page_title': "Edit Tag", 'form': form}
    return render(request, 'home/tag-create-edit.html', context)


def tag_delete(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect('/tag/view')
