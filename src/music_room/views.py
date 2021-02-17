from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import models


def music_room(request):
    return HttpResponse("HELLO")
