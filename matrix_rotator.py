class Solution(object):
    def rotate(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        j = 0
        for i in range(row):
            matrix[i].reverse()
        return matrix
