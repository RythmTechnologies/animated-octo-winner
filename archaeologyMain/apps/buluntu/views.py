
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# Formlar
from .forms import *
from .models import *

# Küçük buluntu formları
from apps.buluntuForm.models import Formlar


from apps.specuser.models import *

# Mixin
from apps.main.mixin import HttpRequest, HttpResponse


# add buluntu starts
@login_required(login_url="homepage")
@require_http_methods(["GET", "POST"])
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}

    context["form"] = GeneralBuluntuForm


    if request.method == "POST":
        print("POST OBJECT:", request.POST)

        incame_data = request.POST

        buyuk_buluntu_form = GeneralBuluntuForm(incame_data)

        kucuk_buluntu_form_instance = Formlar.objects.get(id = int(incame_data['buluntuForms']))
        kucuk_buluntu_form = CombinedForms(instance=kucuk_buluntu_form_instance)
            
        context["errors"] = {}

        if buyuk_buluntu_form.is_valid():

            buyuk_buluntu_form = buyuk_buluntu_form.save(commit=False)
            buyuk_buluntu_form.processedBy = request.user
            buyuk_buluntu_form.save()

        else:
            context["errors"]["buluntuForm"] = buyuk_buluntu_form.errors
            context['form'] = buyuk_buluntu_form
            # return render(request, "buluntu/create.html", context)
        

        if kucuk_buluntu_form.is_valid():
            kucuk_buluntu_form.update_fields(incame_data, kucuk_buluntu_form_instance)

        else:
            print("kücük buluntu formunda hatalar:", kucuk_buluntu_form.errors)
            kucuk_buluntu_form.update_fields(incame_data, kucuk_buluntu_form_instance)

        return redirect('dashboard')
    

    elif request.method == "GET":

        return render(request, "buluntu/create.html", context)
# ends


from apps.buluntuForm.forms import *

@require_http_methods(["GET", "POST"])
def get_buluntu_form(request: HttpRequest, formId: int) -> HttpResponse:

    data = {}
    data['form'] = {}

    print("FORM ID:", formId)
    # TODO FORMLARA GORE OZEL ALANLARIN GELMESI
    try:

        kucuk_buluntu = Formlar.objects.get(id = formId)
        data['buluntu'] = kucuk_buluntu


        form = CombinedForms(kucuk_buluntu)
        data['buluntuform'] = form

        
        # related_name chain yapıalcak

    except Exception as e:
         print("FORMU ALIRKEN HATA:", e)
         data['error'] = {"response": "Böyle bir buluntu mevcut değil."}


    return render(request, 'buluntu/Components/BuluntuModal.html', data)





@require_http_methods(["GET"])
def get_buluntu_test(request: HttpRequest) -> HttpResponse:
     
     context = {}
     context["form"] = GeneralBuluntuForm

     x = Formlar.objects.all()
     context['buluntuForms'] = x


     return render(request, 'buluntu/create.html', context)
     
