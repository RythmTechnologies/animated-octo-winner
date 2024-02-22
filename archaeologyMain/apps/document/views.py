from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from apps.main.mixin import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from .filters import DocumentFilter
from .forms import *
from .models import *
from xhtml2pdf import pisa
import io




# Document Start
@login_required(login_url="homepage")
def get_document(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save_with_log(user=request.user)
            messages.success(request, "Rapor Başarıyla Eklenmiştir!")
            return redirect("document-liste")
        else:
            print("Forms Errors:", form.errors)
            messages.error(request, "Lütfen Form'u Eksiksiz Doldurunuz!")
            return redirect("set-document")
    else:
        form = DocumentForm(user=request.user)

    return render(request, "document/create.html", {"form": form})


@login_required(login_url="homepage")
def get_document_list(request):
    document_list = DocumentCreateModel.objects.all().defer('file')
    document_filter = DocumentFilter(request.GET, queryset=document_list)


    paginator = Paginator(document_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    updateForms = {document.id: DocumentForm(instance=document) for document in page_obj}

    context = {
        "form": document_filter.form,
        "documents": page_obj,
        "updateForms": updateForms
    }

    return render(request, "document/list.html", context)


@login_required(login_url="homepage")
def delete_document(request: HttpRequest, id : int) -> HttpResponseRedirect:
    try:
        document = DocumentCreateModel.objects.filter(id = id ).first()
        if request.user.is_authenticated and request.user.is_superuser or request.user.isModerator:
            document.user = request.user
            document.delete_with_log(user=request.user)
            return redirect("document-liste")
    except Exception as error:
        print("Hata Mesajı Document Silinme", error)

@login_required(login_url="homepage")
def update_document(request: HttpRequest, id : int) -> HttpResponseRedirect:
    document = DocumentCreateModel.objects.get(id=id)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            print("gelen error",form.errors)
            document = form.save(commit=False)
            document.user = request.user
            document.save_with_log(user=request.user)
            return redirect("document-liste")
        else:
            messages.error(request, "Lütfen Formu Doğru Giriniz!")
            return redirect("document-liste")
# Document End

# Print PDF Start
@login_required(login_url="homepage")
def get_html_content(request,id):
    # Belirli bir document_id için belgeyi al
    document = DocumentCreateModel.objects.get(id=id)
    html_content = render_to_string('document/print.html', {'document': document})
    return HttpResponse(html_content, content_type="text/html")