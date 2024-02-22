from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Fixture
from .filters import FixtureFilter
from .forms import FixtureForm
from apps.specuser.models import SiteUser
from apps.main.mixin import HttpRequest, HttpResponse,HttpResponseRedirect
from django.template.loader import render_to_string

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
            form.save(user=request.user)
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

        fixture.delete_with_log(user=request.user)

        messages.success(request,f'Demirbaşınız silindi')

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
            updated_fixture = form.save(commit=False)
            updated_fixture.save(user=request.user)
            return redirect("fixture-liste")
        else:
            messages.error(request, "Lütfen Formu Doğru Giriniz")
            return redirect("fixture-liste")


# Demirbaş End
@login_required(login_url="homepage")
def get_html_content(request,id):
    
    fixture = Fixture.objects.get(id=id)
    html_content = render_to_string('fixture/print.html', {'fixture': fixture})
    return HttpResponse(html_content, content_type="text/html")