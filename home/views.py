from django.shortcuts import render, redirect, get_object_or_404
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotFound,
    Http404,
)
from .models import Author, Tag, Action, Comment
from .forms import ActionForm, TagForm, CommentForm
from django.urls import reverse

# Create your views here.


def index(request):
    actions = Action.objects.all().order_by("-created_time")  # 내림차 정렬
    context = {"page_title": "Home", "actions": actions}
    return render(request, "home/index.html", context)


# 미지의 세계: 사용자 인증 기능 + 소셜 로그인 + 권한 별 기능 제한
def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")


# 설정(팝업, 알람, 시간)
def setting(request):
    return HttpResponse("setting")


# 기준에 따른 검색 및 정렬
def search(request):
    return HttpResponse("search")


def user(request):
    return HttpResponse("user")


def action_create(request):
    # form = ActionForm() # 없어도 되나? 없어도 된다!
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            # ToDo: 현재 사용자가 author가 되도록 처리
            new_action = Action(
                title=form.cleaned_data["title"],
                memo=form.cleaned_data["memo"],
                author=form.cleaned_data["author"],
            )
            new_action.save()  # 여러 저장 방법 중 목적에 따라 사용할 수 있어야 함

            # ManyToMany, 다중선택된 Tag 저장
            tags = form.cleaned_data["tag"]
            new_action.tag.set(tags)

            print("✅ CREATE ACTION")
            return redirect("/")  # name을 사용하면 오류가 나는데 어찌된 영문?
    else:
        form = ActionForm()
    context = {"page_title": "Create Action", "form": form}
    return render(request, "home/action-create-edit.html", context)


def action_edit(request, id):
    action = get_object_or_404(Action, pk=id)
    if request.method == "POST":
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            new_action = Action(
                title=form.cleaned_data["title"],
                memo=form.cleaned_data["memo"],
                author=form.cleaned_data["author"],
            )
            new_action.save()
            tags = form.cleaned_data["tag"]
            new_action.tag.set(tags)
            print("✅ EDIT ACTION")
            return redirect("/")
    else:
        form = ActionForm(instance=action)
    context = {"page_title": "Edit Action", "form": form, "action": action}
    return render(request, "home/action-create-edit.html", context)


def action_delete(request, id):
    action = Action.objects.get(id=id)
    action.delete()
    return redirect("/")


def comment_create(request, action_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # ToDo: 현재 사용자가 author가 되도록 처리
            new_comment = Comment(
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"],
                action=get_object_or_404(Action, pk=action_id),
            )
            new_comment.save()  # 여러 저장 방법 중 목적에 따라 사용할 수 있어야 함
            print("✅ CREATE COMMENT")
            return redirect("/")
    else:
        form = CommentForm()
    context = {"page_title": "Create Comment", "form": form, "action_id": action_id}
    return render(request, "home/comment-create.html", context)


def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect("/")


def tag_view(request):
    tags = Tag.objects.all().order_by("title")
    context = {"page_title": "Tag", "tags": tags}
    return render(request, "home/tag-view.html", context)


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = Tag(title=form.cleaned_data["title"])
            new_tag.save()
            print("✅ CREATE TAG")
            return redirect("/tag/view/")
    else:
        form = TagForm()
    context = {"page_title": "Create Tag", "form": form}
    return render(request, "home/tag-create-edit.html", context)


def tag_edit(request, id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            new_tag = Tag(title=form.cleaned_data["title"])
            new_tag.save()
            print("✅ EDIT TAG")
            return redirect("/tag/view/")
    else:
        form = TagForm(instance=tag)
    context = {"page_title": "Edit Tag", "form": form}
    return render(request, "home/tag-create-edit.html", context)


def tag_delete(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect("/tag/view")
