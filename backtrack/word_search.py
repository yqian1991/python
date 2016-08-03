class Solution(object):
    def check(self, word, i, j, word_index, board, guard, direction):
        if word_index == len(word):
            return True

        rows = len(board)
        cols = len(board[0])

        if j-1 > 0 and direction != 'right' and board[i][j-1] == word[word_index] and not guard[cols*i+j-1]:
            guard[cols*i+j-1] = True
            if self.check(word, i, j-1, word_index+1, board, guard, 'left'):
                return True
            guard[cols*i+j-1] = False

        if j+1<cols and direction != 'left' and board[i][j+1] == word[word_index] and not guard[cols*i+j+1]:
            guard[cols*i+j+1] = True
            if self.check(word, i, j+1, word_index+1, board, guard, 'right'):
                return True
            guard[cols*i+j+1] = True

        if i+1<rows and direction != 'up' and board[i+1][j] == word[word_index] and not guard[cols*(i+1)+j]:
            guard[cols*(i+1)+j] = True
            if self.check(word, i+1, j, word_index+1, board, guard, 'down'):
                return True
            guard[cols*(i+1)+j] = False

        if i-1>0 and direction != 'down' and board[i-1][j] == word[word_index] and not guard[cols*(i-1)+j]:
            guard[cols*(i-1)+j] = True
            if self.check(word, i-1, j, word_index+1, board, guard, 'up'):
                return True
            guard[cols*(i-1)+j] = False
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        if rows > 0:
            cols = len(board[0])
        else:
            return False

        guard = [False]*rows*cols
        word_index = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == word[word_index]:
                    print board[i][j], ' ', j
                    guard[cols*i+j] = True
                    if self.check(word, i, j, word_index+1, board, guard, 'all'):
                        return True
                    guard[cols*i+j] = False
        return False

if __name__ == '__main__':
    sol = Solution()
    board = ["ab"]
    print sol.exist(board, "ba")