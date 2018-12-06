from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
import ssl
from django.core.paginator import Paginator
from django.contrib.auth import login as authorize
from django.contrib.auth import logout as authorize_logout

from db.models import Type
from db.models import ChatRecord

def getWeather (request):
  ip = request.GET["ip"]
  host = "https://ali-weather.showapi.com"
  path = "/ip-to-weather"
  method = "GET"
  appcode = "7be8f8f70a2d47b88d3d1ab5bd9b2e8d"
  querys = "ip=" + ip + "&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0"
  bodys = {}
  url = host + path + "?" + querys

  context = ssl._create_unverified_context()

  _request = urllib.request.Request(url)
  _request.add_header("Authorization", "APPCODE " + appcode)

  with urllib.request.urlopen(_request, context=context) as response:
    data = response.read()
    status = response.status
    reason = response.reason
    
  if status == 200:
    return HttpResponse(data.decode("utf-8"), content_type="application/json; charset=utf-8")
  else:
    response = {
      "reason": reason,
    }
    
    return HttpResponseServerError(reason, content_type="application/json; charset=utf-8")
  
def getTypes (request):
  per_page = request.GET["per_page"]
  curr_page = request.GET["curr_page"]
  name = request.GET["name"]

  types = Types.objects.filter(name__contains = name)
  paginator = Paginator(types, per_page)
      
  response = {
    "list": paginator.page(curr_page),
    "per_page": per_page,
    "curr_page": curr_page,
    "count": paginator.count,
    "name": name
  }
  
  return HttpResponse(response)

def addType (request):
  name = request.POST["name"]
  keywords = request.POST["keywords"]

  if name == None:
    response = {
      "errorMsg": "类型名称不可为空",
    }

    return HttpResponseNotAllowed(response)

  if keywords == None:
    keywords = ""

  add = Type(name = name, keywords = keywords)
  add.save()
  add.id

  response = {
    id: add.id
  }

  return HttpResponse(response)

def updateType (request):
  id = request.POST["id"]
  name = request.POST["name"]
  keywords = request.POST["keywords"]

  if id == None:
    response = {
      errorMsg: "类型id不可为空"
    }

    return HttpResponseNotAllowed(response)

  if name == None:
    response = {
      errorMsg: "类型名称不可为空"
    }

    return HttpResponseNotAllowed(response)

  type = Type.objects.get(id = id)
  type.name = name
  type.keywords = keywords
  type.save()

  response = {
    "msg": "更新类型成功"
  }

  return HttpResponse(response)

def deleteTypes (request):
  ids = request.POST["ids"]

  if ids == None:
    response = {
      "errorMsg": "ids不可为空"
    }

    return HttpResponseNotAllowed(response)

  for id in ids:
    Type.objects.filter(id = id).delete()

  response = {
    "msg": "删除成功"
  }

  return HttpResponse(response)



def getChatRecords (request):
  per_page = request.GET["per_page"]
  curr_page = request.GET["curr_page"]
  type = request.GET["type"]
  start_at = request.GET["start_at"]
  end_at = request.GET["end_at"]

  types = ChatRecord.objects.filter(type__contains = type).filter(create_at__gte = start_at).filter(type__lte = end_at)
  paginator = Paginator(types, per_page)
      
  response = {
    "list": paginator.page(curr_page),
    "per_page": per_page,
    "curr_page": curr_page,
    "count": paginator.count,
    "name": name
  }
  
  return HttpResponse(response)

def sendMessage (request):
  id = request.META["REMOTE_ADDR"]
  content = request.POST["content"]

  if content == None:
    response = {
      "errorMsg": "消息内容不可为空",
    }

    return HttpResponseNotAllowed(response)

  add = ChatRecord(id = id, content = content)
  add.save()
  add.id

  response = {
    id: add.id
  }

  return HttpResponse(response)
