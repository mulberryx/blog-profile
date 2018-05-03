# -*- coding: UTF-8 -*-

from Crawler import Crawler

crawlerTasksDict = {}

'''
  * 开始爬虫任务
  * @param {string} 目标站点的 url
  * @param {object} 爬虫任务配置项
  * @return {boolean} 是否成功 
'''
def startCrawlerTask (url, options):
  crawlerTask = CrawlerTask(url, options)
  crawlerTasksDict[crawlerTask.id] = crawlerTask
  
  return crawlerTask.start()

'''
  * 结束爬虫任务
  * @param {string} 爬虫任务的id
  * @return {boolean} 是否成功
'''
def stopCrawlerTask (id):
  crawlerTask = crawlerTasksDict[id]
  return crawlerTask.stop()

'''
  * 暂停爬虫任务
  * @param {string} 爬虫任务的id
  * @return {boolean} 是否成功
'''
def pauseCrawlerTask (id):
  crawlerTask = crawlerTasksDict[id]
  return crawlerTask.pause()

'''
 * 获取当前有效的爬虫任务列表
 * @return {List} 爬虫任务列表
'''
def getCrawlerTasks ():
  crawlerTasksList = []
  for key in crawlerTasksDict:
    crawlerTasksList.append(crawlerTasksDict[key])
  
  return crawlerTasksList
