from django.shortcuts import render, redirect
from .forms import DynamicForm
from apps.main.mixin import HttpRequest, RedirectOrResponse


def custom_form_view(request: HttpRequest) -> RedirectOrResponse:
    form = DynamicForm()
    if request.method == "POST":
        form = DynamicForm(request.POST)
        if form.is_valid():
            if form.user:
                form.save(commit=false)
                form.user = request.user
                form.save()
                return redirect("custom-form")
            else:
                form.save()
                return redirect("custom-form")
        else:
            return redirect("homepage")

    return render(request, "testfield/custom_form.html", {"form": form})
