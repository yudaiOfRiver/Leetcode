class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binarySearch(mat):
            l, r = 0, len(mat)-1
            while l <= r:
                m = (l+r) // 2
                if mat[m] == target:
                    return "true"
                elif mat[m] < target:
                    l = m+1
                elif mat[m] > target:
                    r = m-1
            return "false"

        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            if matrix[row][0] <= target <= matrix[row][cols-1]:
                return binarySearch(matrix[row])
        return "false"



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
## Output: false
obj = Solution()
print(obj.searchMatrix(matrix, target))
