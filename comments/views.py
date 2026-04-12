from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment
import bleach
import os


def index(request):
    return HttpResponse("Головна")


def comment_list(request):
    sort = request.GET.get("sort", "-created_at")

    allowed = [
        "username",
        "-username",
        "email",
        "-email",
        "created_at",
        "-created_at",
    ]

    if sort not in allowed:
        sort = "-created_at"

    comments = Comment.objects.filter(parent=None).order_by(sort)

    for c in comments:
        if c.file:
            c.filename = os.path.basename(c.file.name)
        else:
            c.filename = None

    paginator = Paginator(comments, 25)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    return render(
        request,
        "comments/list.html",
        {"page_obj": page_obj, "current_sort": sort},
    )


def comment_create(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/comments/#comment-{comment.id}")
    else:
        form = CommentForm()

    return render(request, "comments/create.html", {"form": form})


def comment_reply(request, pk):
    parent = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = parent
            comment.save()

            return redirect(f"/comments/#comment-{parent.id}")
    else:
        form = CommentForm()

    return render(
        request,
        "comments/create.html",
        {"form": form, "parent": parent},
    )


def comment_preview(request):
    if request.method == "POST":
        text = request.POST.get("text", "")

        clean = bleach.clean(
            text,
            tags=["a", "code", "i", "strong"],
            attributes={"a": ["href", "title"]},
            strip=True,
        )

        return JsonResponse({"preview": clean})

    return JsonResponse({"preview": ""})


def file_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    content = None
    filename = None

    if comment.file:
        filename = os.path.basename(comment.file.name)

        if comment.file.name.lower().endswith(".txt"):
            try:
                with comment.file.open("rb") as file:
                    content = file.read().decode("utf-8")
            except UnicodeDecodeError:
                content = "Не вдалося прочитати файл (encoding error)"

    return render(
        request,
        "comments/file.html",
        {
            "comment": comment,
            "content": content,
            "filename": filename,
        },
    )
