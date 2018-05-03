# -*- coding: UTF-8 -*-
import uuid
from Crawler import Crawler

class CrawlerTask:
  '''
   * 构造函数
   * @param {string} url
   * @param {object} 配置对象
   * @constructor
  '''
  def __init__ (self, url, options):
    self.id = uuid.uuid1()
    self.crawler = Crawler(url, options.crawlerOptions)
  
  '''
   * 开始任务
   * @return {boolean} 是否成功
  '''
  def start ():
    return 
  
  '''
   * 停止任务
   * @return {boolean} 是否成功
  '''
  def stop ():
    
  '''
   * 暂停任务
   * @return {boolean} 是否成功
  '''
  def pause ():
  
