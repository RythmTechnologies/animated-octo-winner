
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
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
@require_http_methods(["GET", "POST"])
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}

    buluntuFormObject = {}
   
    
    # test purpose
    buluntuFormObject["1"] = PismikToprakForm()
    buluntuFormObject["2"] = KemikForm()
    buluntuFormObject["5"] = C14Form()
    buluntuFormObject["6"] = ToprakForm()
    buluntuFormObject["7"] = CanakComlekForm()
    

    context["form"] = GeneralBuluntuForm
    context['buluntuForms'] = buluntuFormObject
    
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
            context['form'] = buluntuForm
            return render(request, "buluntu/create.html", context)

    elif request.method == "GET":

        return render(request, "buluntu/create.html", context)
# ends


