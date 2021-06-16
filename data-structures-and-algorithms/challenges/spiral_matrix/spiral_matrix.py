class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1 for i in range(n)] for j in range(n)]
        start_row = start_column = 0
        end_row = end_column = n
        num = 1
        
        while start_row < end_row and start_column < end_column:
            for i in range(start_column, end_column):
                matrix[start_row][i] = num
                num += 1
            start_row += 1
            
            for i in range(start_row, end_row):
                matrix[i][end_column-1] = num
                num += 1
            end_column -= 1
            
            for i in range(end_column-1, start_column-1, -1):
                matrix[end_row-1][i] = num
                num += 1
            end_row -= 1
            
            for i in range(end_row-1, start_row-1, -1):
                matrix[i][start_column] = num
                num += 1
            start_column += 1
            
        return matrix
