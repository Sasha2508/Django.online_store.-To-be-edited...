from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *


def index(request):
    return HttpResponse('This is testing response!')