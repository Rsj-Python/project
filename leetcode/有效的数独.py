class Solution():
    def isValidSudoku(self,List):
        i = x = m = a = k = z = 0
        n = 3
        new_list1 = [[] for i in range(9)]
        new_list2 = [[] for i in range(9)]
        while i < 9:
            for s in List[i]:
                if s != '.' and List[i].count(s) > 1:
                    return False
            i += 1
        while x < 9:
            for j in range(9):
                new_list1[x].append(List[j][x])
            x += 1
        while k < 9:
            for s in new_list1[k]:
                if s != '.' and new_list1[k].count(s) > 1:
                    return False
            k += 1
        for j in range(9):
            new_list2[j].append(List[a][m:n] + List[a + 1][m:n] + List[a + 2][m:n])
            m += 3
            n += 3
            if n > 9:
                a += 3
                m = 0
                n = 3
        while z < 9:
            for nb in new_list2[z][0]:
                if nb != '.' and new_list2[z][0].count(nb) > 1:
                    return False
            z += 1
        return new_list2
my = Solution()
List = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
print(my.isValidSudoku(List))
