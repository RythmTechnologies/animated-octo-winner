
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# Formlar
from .forms import *
from .models import *

from apps.specuser.models import *

# Mixin
from apps.main.mixin import HttpRequest, HttpResponse


# add buluntu starts
@login_required(login_url="homepage")
@require_http_methods(["GET", "POST"])
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}

    buluntuFormObject = {}


    context["form"] = GeneralBuluntuForm
    context['buluntuForms'] = buluntuFormObject

    if request.method == "POST":
        print("POST OBJECT:", request.POST)

        incame_data = request.POST

        buluntuForm = GeneralBuluntuForm(incame_data)

        context["errors"] = {}

        if buluntuForm.is_valid():

            buluntuForm = buluntuForm.save(commit=False)
            buluntuForm.processedBy = request.user
            buluntuForm.save()

            return redirect("dashboard")

        else:
            context["errors"]["buluntuForm"] = buluntuForm.errors
            context['form'] = buluntuForm
            return render(request, "buluntu/create.html", context)

    elif request.method == "GET":

        return render(request, "buluntu/create.html", context)
# ends


@require_http_methods(["GET"])
def get_buluntu_form(request: HttpRequest, id: int) -> HttpResponse:
    context = {}
    buluntuFormObject = {}

    if id == '1':
        buluntuFormObject["1"] = PismikToprakForm()
    elif id == '2':
         buluntuFormObject["2"] = KemikForm()
    elif id == '5':
        buluntuFormObject["5"] = C14Form()
    elif id == "6":
            buluntuFormObject["6"] = ToprakForm()
    elif id == '7':
           buluntuFormObject["7"] = CanakComlekForm()

    context['buluntuForms'] = buluntuFormObject



    return render(request, 'buluntu/Components/BuluntuModal.html', context)
