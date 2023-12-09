from django.shortcuts import render


#For TypeHint
import typing as t
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


# Example typehint func
"""
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'templatename.html')
"""
