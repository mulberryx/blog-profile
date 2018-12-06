from django.db import models
import django.utils.timezone as timezone

# 消息类型
class Type (models.Model):
  # 类型名称
  name = models.CharField(max_length = 20, null = False)

  # keywords
  keywords = models.CharField(max_length = 80, null = True)

# 聊天记录
class ChatRecord(models.Model):
  # 聊天者的ip
  ip = models.CharField(max_length = 15, null = False)

  # 消息内容
  content = models.CharField(max_length = 80, null = False)

  # 消息类型
  type = models.ForeignKey(Type, on_delete = models.DO_NOTHING, null = True)

  # 保存日期
  create_at = models.DateTimeField(default = timezone.now)
  
  # 最后修改日期
  update_at = models.DateTimeField(auto_now = True)

