# -*- coding: UTF-8 -*-

# 打断
I_1 = 5
I_2 = 6
I_3 = 12
I_4 = 100

# 隔空 1 打断
I_1_1 = 
I_1_2 = 
I_1_3 = 

# 隔空 2 打断
I_2_1 = 
I_2_2 = 
I_2_3 = 

# 隔空 3 打断
I_3_1 = 
I_3_2 = 
I_3_3 = 

# 单边
S_1 = 
S_2 = 
S_3 = 
S_4 = 

# 单边隔空 1 被堵
S_1_1 = 0
S_1_2 = 0
S_1_3 = 0
S_1_4 = 7

# 单边隔空 2 被堵
S_2_1 = 
S_2_2 = 
S_2_3 = 
S_2_4 = 

# 双边
D_1 = 
D_2 = 
D_3 = 
D_4 = 

# 双边隔空 1 被堵
D_1_1 = 
D_1_2 = 
D_1_3 = 
D_1_4 = 

# 双边隔空 2 被堵
D_2_1 = 
D_2_2 = 
D_2_3 = 
D_2_4 = 

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
  return 0

"""
 * 计算方向权重
 * @param {Grid []} 当前方向的格子
 * @param {Grid} 当前格子
 * @return {number} 当前方向权重
"""
def caculateDirectionWeight (grids, grid):
  return 0
