class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1

        for i in range(0, len(matrix)):
            if (matrix[i][0] <= target <= matrix[i][len(matrix[i])-1]):
                target_row = i
                break

        if target_row == -1:
            return False

        left = 0
        right = len(matrix[target_row])

        while(left <= right):
            mid = (left + right) // 2
            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
                return True

        return False
