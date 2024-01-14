
from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Fixture
from .filters import FixtureFilter
from .forms import FixtureForm
from apps.account.models import SiteUser

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

    context = {"form": fixture_filter.form, "fixtures": fixture_filter.qs}

    return render(request, "fixture/list.html", context)

# Demirbas Add end