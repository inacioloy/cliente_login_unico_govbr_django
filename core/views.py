from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.shortcuts import render
from cliente_login_unico_govbr_django import settings


def index(request):
    return render(request, 'index.html', {})

@login_required()
def logout(request):
    try:
        django_logout(request)
    except Exception:
        pass
    url = settings.LOGOUT_URL_GOV_BR
    return HttpResponseRedirect(url)
