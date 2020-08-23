matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
class Solution():
    def rotate(self,matrix):
        new_list = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_list[i].append(matrix[j][i])
            new_list[i] = new_list[i][::-1]
        for i in range(len(matrix)):
            matrix[i] = new_list[i]
my = Solution()
my.rotate(matrix)