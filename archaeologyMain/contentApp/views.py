from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from .models import Fixture
from .filters import FixtureFilter, RaporAcmaFilter, DocumentFilter

# Formlar
from .forms import *
from userApp.models import *

# For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# Homepage start


def get_index(request: HttpRequest) -> RedirectOrResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            userLogin = authenticate(request, username=username, password=password)

            if userLogin is not None:
                login(request, userLogin)

                # Message Success
                messages.success(
                    request, f"Login Correct! Welcome {request.user.username}!"
                )
                return redirect("dashboard")
            else:
                # Message Error
                messages.error(request, "The username or password is incorrect")
                return redirect("homepage")
        else:
            # Message Warning
            messages.warning(request, "Please fill in the fields.")
            return redirect("homepage")

    return render(request, "index.html")


# Homepage End


# Dashboard Start
@login_required(login_url="homepage")
def get_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard.html")


# Dashboard End


# add buluntu starts
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST":
        print("POST OBJECT:", request.POST)

        incame_data = request.POST

        buluntuForm = GeneralBuluntuForm(incame_data)
        instruactionForm = GeneralInstructionsForm(incame_data)
        imageForm = BuluntuImagesForm(incame_data, request.FILES)
        minorForm = MinorBuluntuForm(incame_data)

        context["errors"] = {}

        if (
            buluntuForm.is_valid()
            and instruactionForm.is_valid()
            and imageForm.is_valid()
            and minorForm.is_valid()
        ):
            buluntuForm.save()
            instruactionForm.save()
            imageForm.save()
            minorForm.save()

            return redirect("dashboard")

        else:
            context["errors"]["buluntuForm"] = buluntuForm.errors
            context["errors"]["instruactionForm"] = instruactionForm.errors
            context["errors"]["imageForm"] = imageForm.errors
            context["errors"]["minorBuluntuForm"] = minorForm.errors

            context["form"] = GeneralBuluntuForm
            context["instruactionForm"] = GeneralInstructionsForm
            context["imageForm"] = BuluntuImagesForm
            context["minorBuluntuForm"] = MinorBuluntuForm

            return render(request, "Buluntu/create.html", context)

    elif request.method == "GET":
        context["form"] = GeneralBuluntuForm
        context["instruactionForm"] = GeneralInstructionsForm
        context["imageForm"] = BuluntuImagesForm
        context["minorBuluntuForm"] = MinorBuluntuForm
        return render(request, "Buluntu/create.html", context)


# ends


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

    return render(request, "Fixture/create.html", context)


# Demirbas Add end


@login_required(login_url="homepage")
def fixture_list(request: HttpRequest) -> HttpResponse:
    fixture_filter = FixtureFilter(request.GET, queryset=Fixture.objects.all())

    context = {"form": fixture_filter.form, "fixtures": fixture_filter.qs}

    return render(request, "Fixture/list.html", context)


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

    return render(request, "Rapor/create.html", {"form": form})


@login_required(login_url="homepage")
def get_rapor_list(request: HttpRequest) -> HttpResponse:
    rapor_filter = RaporAcmaFilter(request.GET, queryset=AcmaRapor.objects.all())

    context = {"form": rapor_filter.form, "rapors": rapor_filter.qs}

    return render(request, "Rapor/list.html", context)


# Rapor End


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
            return redirect("rapor-liste")
        else:
            print("Forms Errors:", form.errors)
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect("set-rapor")
    else:
        form = DocumentForm(user=request.user)

    return render(request, "Document/create.html", {"form": form})


@login_required(login_url="homepage")
def get_document_list(request: HttpRequest) -> HttpResponse:
    document_filter = DocumentFilter(
        request.GET, queryset=DocumentCreateModel.objects.all()
    )

    context = {"form": document_filter.form, "documents": document_filter.qs}

    return render(request, "Document/list.html", context)


# Document End


# 404 Page Start
def get_notFound(request: HttpRequest) -> HttpResponse:
    return render(request, "404page.html")


# 404 Page End
