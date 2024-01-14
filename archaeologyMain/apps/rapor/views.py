from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]

from .forms import AcmaRaporForm
from .filters import RaporAcmaFilter
from .models import *



# Rapor Start
def get_rapor(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AcmaRaporForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            rapor = form.save(commit=False)
            rapor.user = request.user
            rapor.save()
            messages.success(request, "Rapor Başarıyla Eklenmiştir!")
            return redirect("rapor-liste")
        else:
            print("Forms Errors:", form.errors)
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect("set-rapor")
    else:
        form = AcmaRaporForm(user=request.user)

    return render(request, "rapor/create.html", {"form": form})


@login_required(login_url="homepage")
def get_rapor_list(request: HttpRequest) -> HttpResponse:
    rapor_filter = RaporAcmaFilter(request.GET, queryset=AcmaRapor.objects.all())

    context = {"form": rapor_filter.form, "rapors": rapor_filter.qs}

    return render(request, "rapor/list.html", context)


# Rapor End