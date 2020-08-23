class Solution:
    def __init__(self):
        pass
    def removeDuplicates(self, List) -> int:
        i = 0
        if len(List) == 0:
            return 0
        else:
            for j in range(1,len(List)):
                if List[i] != List[j]:
                    List[i+1] = List[j]
                    i += 1
            return i + 1
mysolution = Solution()
print(mysolution.removeDuplicates([1,1,2]))










