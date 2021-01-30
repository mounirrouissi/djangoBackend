from django.shortcuts import render

from .forms import ReservationForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Festival
from .serializers import festivalsSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import festivalsSerializers, reservationSerializers
from rest_framework.response import Response
from api.models import Festival, Reservation




@api_view(['GET', 'POST', 'DELETE'])
class FestivalViewSet(viewsets.ModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = festivalsSerializers
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = reservationSerializers


def sendData(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']
            city = form.cleaned_data['city']
            places = form.cleaned_data['places']
            category = form.cleaned_data['category']
        print(name, status, city)

    form = ReservationForm()
    return render(request, 'templates/form.html', {'form': form})
