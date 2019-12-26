'''
    棋局
    @Class
    @author Philip
'''
import json
from services.gobang.Chessboard import Chessboard

class Gobang:
    chessboard = None
    player = None
    playerLastStep = None
    computerLastStep = None

    '''
        构造函数
        @__init__
    '''
    def __init__(self, player):
        self.chessboard = Chessboard()
        self.player = player

    '''
        落子
        @param {piece} 步对象
        @return void
    '''
    def putPiece (self, step):
        self.playerLastStep = step
        self.chessboard.putPicec(step)

    '''
        电脑计算下一步
        @return void
    '''
    def computeStep (self):
        pass

    '''
        获取棋盘 json
        @return {json} 记录黑白子位置的json对象
    '''
    def getChessboardJson(self):
        chessboardJson = []
        chessboardData = self.chessboard.getData()

        for idx in chessboardData:
            for _idx in chessboardData[idx]:
                piece = chessboardData[idx][_idx]
                chessboardJson[idx][_idx] = piece.color()


        return json.dumps(chessboardJson)
    '''
        悔棋
        @return void
    '''
    def regret (self):
        self.chessboard.removePiece(self.playerLastStep)
        self.chessboard.removePiece(self.computerLastStep)
