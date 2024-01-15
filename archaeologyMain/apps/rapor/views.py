from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


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


login_required(login_url="homepage")
def delete_rapor(request: HttpRequest, id: int) -> HttpResponseRedirect:
    try:
        rapor = AcmaRapor.objects.get(id=id)
        if request.user.is_authenticated and request.user.is_superuser and request.user.isModerator:
            rapor.delete()
            return redirect("rapor-list")
    except Exception as e:
        print("Hata Silme", e)


@login_required(login_url="homepage")
def get_rapor_list(request):
    rapor_filter = RaporAcmaFilter(request.GET, queryset=AcmaRapor.objects.all())
    updateForms = {rapor.id: AcmaRaporForm(instance=rapor) for rapor in rapor_filter.qs}
    context = {
        "form": rapor_filter.form,
        "rapors": rapor_filter.qs,
        "updateForms": updateForms
    }
    return render(request, "rapor/list.html", context)

@login_required(login_url="homepage")
def update_rapor(request, id):
    rapor = AcmaRapor.objects.get(id=id)
    if request.method == "POST":
        form = AcmaRaporForm(request.POST, instance=rapor)
        if form.is_valid():
            form.save()
            return redirect('rapor-liste')
        else:
            messages.error(request, "Lütfen Formu Doğru Giriniz!")
            return redirect('rapor-liste')