from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Fixture
from .filters import FixtureFilter
from .forms import FixtureForm
from apps.specuser.models import SiteUser

# For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# Demirbas Add Start
@login_required(login_url="homepage")
def set_fixture(request: HttpRequest) -> HttpResponse:
    context = {}
    creater = SiteUser.objects.filter(id=request.user.id).first()
    serverForm = FixtureForm()
    context["form"] = serverForm

    if request.method == "POST":
        form = FixtureForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = creater
            form.save()
            messages.success(request, "Demirbaş Başarıyla Eklenmiştir!")
            return redirect("fixture-liste")
        else:
            print("Form Errors:", form.errors)
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect("set-fixture")

    return render(request, "fixture/create.html", context)


@login_required(login_url="homepage")
def fixture_list(request: HttpRequest) -> HttpResponse:
    fixture_filter = FixtureFilter(request.GET, queryset=Fixture.objects.all())
    paginator = Paginator(fixture_filter.qs, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    updateForms = {
        fixture.id: FixtureForm(instance=fixture) for fixture in fixture_filter.qs
    }
    context = {
        "form": fixture_filter.form,
        "fixtures": page_obj,
        "updateForms": updateForms,
    }

    return render(request, "fixture/list.html", context)


@login_required(login_url="home")
def delete_fixture(request: HttpRequest, id: int) -> HttpResponseRedirect:
    fixture = Fixture.objects.filter(id = id).first()
    if request.user.is_authenticated and request.user.is_superuser or request.user.isModerator:
        fixture.delete()
        return redirect("fixture-liste")
    else:
        messages.error(request, "Lütfen Giriş Yapınız")
        return redirect("homepage")


@login_required(login_url="homepage")
def update_fixture(request: HttpRequest, id: int) -> HttpResponseRedirect:
    fixture = Fixture.objects.get(id = id)
    if request.method == "POST":
        form = FixtureForm(request.POST,request.FILES, instance=fixture)
        if form.is_valid():
            form.save()
            return redirect("fixture-liste")
        else:
            messages.error(request, "Lütfen Formu Doğru Giriniz")
            return redirect("fixture-liste")


# Demirbaş End
