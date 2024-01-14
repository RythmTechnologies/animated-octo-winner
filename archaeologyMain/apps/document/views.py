# For TypeHint
import typing as t

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .filters import DocumentFilter
from .forms import *
from .models import *

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# Document Start
@login_required(login_url="homepage")
def get_document(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            rapor = form.save(commit=False)
            rapor.user = request.user
            rapor.save()
            messages.success(request, "Rapor Başarıyla Eklenmiştir!")
            return redirect("document-liste")
        else:
            print("Forms Errors:", form.errors)
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect("set-document")
    else:
        form = DocumentForm(user=request.user)

    return render(request, "document/create.html", {"form": form})


@login_required(login_url="homepage")
def get_document_list(request: HttpRequest) -> HttpResponse:
    document_filter = DocumentFilter(
        request.GET, queryset=DocumentCreateModel.objects.all()
    )

    context = {"form": document_filter.form, "documents": document_filter.qs}

    return render(request, "document/list.html", context)


# Document End
