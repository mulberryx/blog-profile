# -*- coding: UTF-8 -*-
import json

"""
 * 棋子类
"""
class Piece:
  """
   * 构造函数
   * @param {number} 棋子行
   * @param {number} 棋子列
   * @param {string} 棋子颜色
   * @constrctor
  """
  def __init__(self, i, j, color):
    self.i = i
    self.j = j
    self.color = color
  
  """
   * 获取棋子数据的 JSON 序列化
   * @return {string} 棋子数据JSON序列化
  """
  def getJson(self):
    return json.dumps({ i: self.i, j: self.j, color: self.color })
  
