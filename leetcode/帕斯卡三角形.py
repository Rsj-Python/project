class Solution():
    def generate(self,numRows):
        if numRows < 3:
            new_list = [[1],[1,1]]
            return new_list[0:numRows]
        else:
            new_list = [[] for i in range(numRows)]
            new_list[0],new_list[1] = [1],[1,1]
            for i in range(2,numRows):
                new_list[i].append(1)
                for j in range(1,i):
                    new_list[i].append(new_list[i-1][j-1] + new_list[i-1][j])
                new_list[i].append(1)
            return new_list
my = Solution()
print(my.generate(5))