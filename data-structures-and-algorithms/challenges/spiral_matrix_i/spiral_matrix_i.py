class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []

        rows_start = columns_start = 0
        rows_end, columns_end = len(matrix), len(matrix[0])
        size = rows_end * columns_end

        while True:
            for j in range(columns_start, columns_end):
                output.append(matrix[rows_start][j])
            rows_start += 1
            if len(output) == size:
                break

            for i in range(rows_start, rows_end):
                output.append(matrix[i][columns_end - 1])
            columns_end -= 1
            if len(output) == size:
                break

            for j in range(columns_end-1, columns_start-1, -1):
                output.append(matrix[rows_end-1][j])
            rows_end -= 1
            if len(output) == size:
                break

            for i in range(rows_end-1, rows_start-1, -1):
                output.append(matrix[i][columns_start])
            columns_start += 1
            if len(output) == size:
                break

        return output
