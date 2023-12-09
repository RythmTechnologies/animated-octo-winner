from django.shortcuts import render

#For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# Create your views here.


def get_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')