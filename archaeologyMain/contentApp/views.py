from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from .models import Fixture
from .filters import FixtureFilter

#Formlar
from .forms import *
from userApp.models import *

#For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]



# Homepage start

def get_index(request: HttpRequest) -> RedirectOrResponse:

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            userLogin = authenticate(request, username = username, password = password)

            if userLogin is not None:
                login(request, userLogin)

                # Message Success
                messages.success(request, f'Login Correct! Welcome {request.user.username}!')
                return redirect('dashboard')
            else:

                # Message Error
                messages.error(request, 'The username or password is incorrect')
                return redirect('homepage')
        else:

            # Message Warning
            messages.warning(request, 'Please fill in the fields.')
            return redirect('homepage')

    return render(request, 'index.html')

# Homepage End

# Dashboard Start
@login_required(login_url='homepage')
def get_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard.html')
# Dashboard End


# add buluntu starts
def set_buluntu(request: HttpRequest) -> HttpResponse:
    context = {}
    context['form'] = GeneralBuluntuForm
    context['instruactionForm'] = GeneralInstructionsForm
    context['imageForm'] = BuluntuImagesForm
    context['minorBuluntuForm'] = MinorBuluntuForm
    return render(request, 'Buluntu/create.html', context)
# ends

# Demirbas Add Start
@login_required(login_url='homepage')
def set_fixture(request: HttpRequest) -> HttpResponse:

    context = {}
    creater = SiteUser.objects.filter(id = request.user.id).first()
    serverForm = FixtureForm()
    context['form'] = serverForm

    if request.method == 'POST':
        form = FixtureForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = creater
            form.save()
            messages.success(request, 'Demirbaş Başarıyla Eklenmiştir!')
            return redirect('set-fixture')
        else:
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect('set-fixture')

    return render(request, 'Fixture/create.html', context)
# Demirbas Add end



@login_required(login_url='homepage')
def fixture_list(request: HttpRequest) -> HttpResponse:
    fixture_filter = FixtureFilter(request.GET, queryset=Fixture.objects.all())

    context = {
        'form' : fixture_filter.form,
        'fixtures': fixture_filter.qs
    }


    return render(request, 'Fixture/list.html', context)

class FilterListView(ListView):
    queryset = Fixture.objects.all()
    template_name = 'Fixture/list.html'
    context_object_name = 'fixtures'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FixtureFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


# 404 Page Start
def get_notFound(request: HttpRequest) -> HttpResponse:
    return render(request, '404page.html')
# 404 Page End