from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

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
                messages.success(request, f'"Login Correct! Welcome {request.user.username}!"')
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


# 404 Page Start
def get_notFound(request: HttpRequest) -> HttpResponse:
    return render(request, '404page.html')
# 404 Page End