from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from music_room.models import Room
from chatroom.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.http import JsonResponse
