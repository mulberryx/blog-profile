# -*- coding: UTF-8 -*-

from Checkerboard import Checkerboard
checkerboard = Checkerboard()

"""
 * 获取机器方最优解
 * @param {Piece[]} 当前棋子列表
 * @return {Piece} 机器方最优解棋子
"""
def getOptimalSolution (Pieces)
  checkerboard.sync(Pieces)
  return checkerboard.getOptimalPiece()
