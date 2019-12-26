'''
    步骤
    @Class
    @author Philip
'''
class Step:
    piece = None
    x = None
    y = None

    '''
        @param {piece} 棋子对象
        @param {number} x
        @param {number} y
    '''
    def __init__(self, piece, x, y):
        self.piece = piece
        self.x = x
        self.y = y
