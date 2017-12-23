# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
 
def robot (request):
  context = {}
  context['env'] = 'dev'
  return render(request, 'robot.html', context)

def statistics (request):
  context = {}
  context['env'] = 'dev'
  return render(request, 'statistics.html', context)

def talk (request):
  context = {}
  context['env'] = 'dev'
  return render(request, 'talk.html', context)