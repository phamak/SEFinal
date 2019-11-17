from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from . import models
# These are your helper functions
from .helpers.db_access import get_status_by_id, set_open_by_id, set_reserved_by_id, set_taken_by_id
import datetime

# Create your views here.

# Render the home page
def index(request):
    app_url = request.path
    return render(request, 'home.html', {'app_url': app_url})

