class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                n = board[i][j]
                if n == '.':
                    continue
                
                box_index = (i//3)*3 + j//3

                if n in rows[i] or n in cols[j] or n in boxes[box_index]:
                    return False
                
                rows[i].add(n)
                cols[j].add(n)
                boxes[box_index].add(n)
        return True
                
