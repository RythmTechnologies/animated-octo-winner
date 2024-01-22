
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Formlar
from .forms import *
from .models import *

from apps.specuser.models import *

# For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# add buluntu starts
@login_required(login_url="homepage")
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST":
        print("POST OBJECT:", request.POST)

        incame_data = request.POST

        buluntuForm = GeneralBuluntuForm(incame_data)
        instruactionForm = GeneralInstructionsForm(incame_data)
        imageForm = BuluntuImagesForm(incame_data, request.FILES)
        minorForm = MinorBuluntu(incame_data)

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
            context["errors"]["minorBuluntu"] = minorForm.errors

            context["form"] = buluntuForm
            context["instruactionForm"] = instruactionForm
            context["imageForm"] = imageForm
            context["minorBuluntu"] = minorForm

            return render(request, "buluntu/create.html", context)

    elif request.method == "GET":
        context["form"] = GeneralBuluntuForm
        context["instruactionForm"] = GeneralInstructionsForm
        context["imageForm"] = BuluntuImagesForm
        context["minorBuluntu"] = MinorBuluntu
        context['minorBuluntuForm'] = FinalBuluntuForm

        print("TETO:", FinalBuluntuForm().fields)
        
        return render(request, "buluntu/create.html", context)
# ends


