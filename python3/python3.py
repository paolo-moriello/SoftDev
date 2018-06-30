import sys
import random

M = 5

class Puzzle:
    def __init__(self, board, blocks):
        self.board = board
        self.blocks = blocks
        self.size = len(board)
    
    
    
    def _try_fit_row(self, block_row, i, j):
        if(len(block_row)+j > self.size):
            return False
        
        for b in xrange(len(block_row)):
            if(block_row[b] != ' ' and self.board[i][j+b] != ' '):
                return False

        return True
    
    
    def find_place(self, block):
        pos = []
        
        for i in xrange(self.size-len(block)+1):
            for j in xrange(self.size):
                found = True
                for r in xrange(len(block)):
                    if(self._try_fit_row(block[r], i+r, j)):
                        for c in xrange(len(block[r])):
                            pos.append((i+r, j+c))
                    else:
                        del pos[:]
                        found = False
                        break
                if(found):
                    return pos
                    
        return False
            
            
    def _clean_board(self):
        self.board = [[' ' for i in xrange(M)] for j in xrange(M)]


    def _check_board(self):
        for i in xrange(self.size):
            for j in xrange(self.size):
                if(self.board[i][j] == ' '):
                    return False
        return True


    def insert_block(self, block, pos):
        x = 0
        for r in range(len(block)):
            for c in range(len(block[r])):
                i = pos[x][0]
                j = pos[x][1]
                x += 1
		if(block[r][c] != ' '):
                    self.board[i][j] = block[r][c]


    def print_board(self):
        for i in xrange(self.size):
            for j in xrange(self.size):
                sys.stdout.write(self.board[i][j])
            print('')

    def search(self):
        while(self._check_board() == False):
            random.shuffle(self.blocks)
            for b in range(len(self.blocks)):
                pos = self.find_place(self.blocks[b])
                if(pos == False):
                    break
                self.insert_block(self.blocks[b], pos)
            else:
                continue
            self._clean_board()


def main():
    blocks = []
    for i in range(1, len(sys.argv)):
        f = open(sys.argv[i], "r")
        content = f.read()
        content = content.split("\n")
        blocks.append(filter(None, content))
        
    board = [[' ' for i in xrange(M)] for j in xrange(M)]

    puzzle = Puzzle(board, blocks)
    puzzle.search()
    puzzle.print_board()


if __name__ == "__main__":
    main()

