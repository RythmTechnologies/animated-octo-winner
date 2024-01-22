
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
        
        context["errors"] = {}

        if buluntuForm.is_valid():
            buluntuForm.save()
  
            return redirect("dashboard")

        else:
            context["errors"]["buluntuForm"] = buluntuForm.errors

            context["form"] = buluntuForm

            return render(request, "buluntu/create.html", context)

    elif request.method == "GET":
        context["form"] = GeneralBuluntuForm
        return render(request, "buluntu/create.html", context)
# ends


