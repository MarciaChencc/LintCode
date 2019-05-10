class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        local_matrix = matrix
        if len(matrix) == 0:
            return False
        else:
            local_matrix = self.transformMatrix(local_matrix)
            high = len(local_matrix)-1
            low = 0
            while high >= low:
                mid = (high + low) // 2
                if local_matrix[mid] == target:
                    return True
                elif local_matrix[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1
            return False

    def transformMatrix(self, matrix):
        new_matrix = matrix
        temp = []
        while type(new_matrix[0]) is list:
            for item in new_matrix:
                temp.extend(item)
            new_matrix = temp
            temp = []
        return new_matrix
