# -*- coding: UTF-8 -*-
# 计算范围
maxRange = 3

# 打断
I_1 = 8
I_2 = 9
I_3 = 16
I_4 = 24

# 隔空 1 打断
I_1_1 = 5
I_1_2 = 4
I_1_3 = 3

# 隔空 2 打断
I_2_1 = 3
I_2_2 = 2
I_2_3 = 1

# 单边
S_1 = 3
S_2 = 4
S_3 = 8
S_4 = 12

# 单边隔空 1 被堵
S_1_1 = 0
S_1_2 = 0
S_1_3 = 0
S_1_4 = 7

# 单边隔空 2 被堵
S_2_1 = 0
S_2_2 = 0
S_2_3 = 4
S_2_4 = 9

# 双边
D_1 = 3
D_2 = 9
D_3 = 16
D_4 = 100

# 双边隔空 1 被堵
D_1_1 = 0
D_1_2 = 0
D_1_3 = 1
D_1_4 = 12

# 双边隔空 2 被堵
D_2_1 = 2
D_2_2 = 5
D_2_3 = 7
D_2_4 = 9

directions = {
  north: [[0, 1], [0, 2], [0, 3], [0, 4]],
  south: [[0, -1], [0, -2], [0, -3], [0, -4]],
  west: [[-1, 0], [-2, 0], [-3, 0], [-4, 0]],
  east: [[1, 0], [2, 0], [3, 0], [4, 0]],
  northWest: [[-1, 1], [-2, 2], [-3, 3], [-4, 4]],
  northEast: [[1, 1], [2, 2], [3, 3], [4, 4]],
  southWest: [[-1, -1], [-2, -2], [-3, -3], [-4, -4]],
  southEast: [[1, -1], [2, -2], [3, -3], [4, -4]]
}

"""
 * 计算分数
 * @param {Checkerboard} 棋盘对象
 * @param {Grid} 当前格子
 * @return {number} 点计算出来的分数
"""
def caculatePoints (checkerboard, grid):
  return ergodicAllDirections(checkerboard, grid)

"""
 * 遍历所有直线
 * @param {Checkerboard} 棋盘对象
 * @param {Grid} 当前格子
 * @return {number} 点计算出来的分数
"""
def ergodicAllDirections (checkerboard, grid):
  weight = 0
  
  for key in directions:
    directionGrids = []
    displacements = directions[key]
    for disp in enumerate(displacements):
      i = grid.i + disp[0]
      j = grid.j + disp[1]
      
      directionGrid = checkerboard.getGrid(i, j)
      directionGrids.append(directionGrid)
    
    weight += caculateDirectionWeight(directionGrids, grid)
  return weight

"""
 * 计算方向权重
 * @param {Grid []} 当前方向的格子
 * @param {Grid} 当前格子
 * @return {number} 当前方向权重
"""
def caculateDirectionWeight (grids, grid):
  return 0
