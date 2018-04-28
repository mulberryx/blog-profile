# -*- coding: UTF-8 -*-
from Piece import Piece
from Grid import Grid
from algorithm import *

"""
 * 棋盘类
"""
class Checkerboard:
  # 棋盘二维列表
  board = []
  
  """
   * 构造函数
   * @param {string} 白子身份
   * @constructor
  """
  def __init__ (self, white):
    if (white == "player")
      self.computerColor = "black"
    else
      self.computerColor = "white"
  
    for i in range(1, 15):
      row = []
      for j in range(1, 15):
        grid = Grid (i, j)
      self.board.append(row)
      
  """
   * 根据行列获取棋盘格
   * @param {number} 行
   * @param {number} 列
   * @return {Grid} 棋盘格
  """
  def getGrid (self, i, j):
    return self.board[i][j]
  
  """
   * 同步棋盘
   * @param {Piece []} 棋子列表
   * @return none
  """
  def sync (self, Pieces):
    for row in self.board
      for grid in row
        grid.clean()
    
    for piece in Pieces:
      grid = self.getGrid(piece.i, piece.j)
      grid.putPiece(piece)
 
  """
   * 获取最优的棋子
   * @return {Piece} 最优的棋子
  """
  def getOptimalPiece (self):
    maxPoint = -1
    optimalPiece = ""
    
    for row in self.board
      for grid in row
        gridPoint = algorithm.caculatePoints(self, grid)
        
        if gridPoint > maxPoint
          maxPoint = gridPoint
          optimalPiece = Piece(grid.i, grid.j, self.computerColor)
    
    return optimalPiece
 
