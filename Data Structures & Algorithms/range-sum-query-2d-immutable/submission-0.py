class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix), len(matrix[0])
        self.presum = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(0,len(matrix)):
            result = 0
            for j in range(0,len(matrix[0])):
                result = result + matrix[i][j]
                self.presum[i+1][j+1] = result + self.presum[i][j+1]
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1, col1+1, row2+1, col2+1
        return self.presum[row2][col2]-self.presum[row1-1][col2]-self.presum[row2][col1-1]+self.presum[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)