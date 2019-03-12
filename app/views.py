# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# 机器人页面
def robot (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "robot.html", context)

# 聊天页面
def talk (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "talk.html", context)
