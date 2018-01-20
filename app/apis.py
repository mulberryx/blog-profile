# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib, sys
import ssl

def getWeather (request):
  ip = request.GET['ip'];
  host = 'https://ali-weather.showapi.com'
  path = '/ip-to-weather'
  method = 'GET'
  appcode = '7be8f8f70a2d47b88d3d1ab5bd9b2e8d'
  querys = 'ip=' + ip + '&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0'
  bodys = {}
  url = host + path + '?' + querys
  context = ssl._create_unverified_context()

  _request = urllib.request.Request(url)
  _request.add_header('Authorization', 'APPCODE ' + appcode)

  with urllib.request.urlopen(_request, context=context) as response:
    data = response.read()
    status = response.status
    reason = response.reason
    
  if status == 200:
    return HttpResponse(data.decode('utf-8'), content_type='application/json; charset=utf-8')
  else:
    return HttpResponse(reason)
  
def test (request):
  # 初始化
  response = ""
  response1 = ""
  
  # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
  list = Test.objects.all()
      
  # filter相当于SQL中的WHERE，可设置条件过滤结果
  response2 = Test.objects.filter(id=1) 
  
  # 获取单个对象
  response3 = Test.objects.get(id=1) 
  
  # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
  Test.objects.order_by('name')[0:2]
  
  #数据排序
  Test.objects.order_by("id")
  
  # 上面的方法可以连锁使用
  Test.objects.filter(name="runoob").order_by("id")
  
  # 输出所有数据
  for var in list:
      response1 += var.name + " "
  response = response1
  return HttpResponse("<p>" + response + "</p>")

def messageList (request):
  return HttpResponse("<p>" + response + "</p>")

def messageAdd (request):
  return HttpResponse("<p>" + response + "</p>")

def messageDelete (request):
  return HttpResponse("<p>" + response + "</p>")

def talk (request):
  return HttpResponse("<p>" + response + "</p>")
