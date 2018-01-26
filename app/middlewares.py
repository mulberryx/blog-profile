import json
import re
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

EXEMPT_URLS=[settings.LOGIN_URL.lstrip('/')]
  
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
  EXEMPT_URLS += settings.LOGIN_EXEMPT_URLS

class authorization (MiddlewareMixin):
  def process_request (self, request):
    if "user" not in request:
      path = request.path_info.lstrip('/')

      if not any(url == path for url in EXEMPT_URLS):
        if re.match("api/", path):
          response = {
            "msg": "您还未登录"
          }

          return HttpResponseForbidden(json.dumps(response), content_type="application/json; charset=utf-8")
        else:
          return HttpResponseRedirect("/admin/login")
