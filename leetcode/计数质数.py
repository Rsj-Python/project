class Solution():
    def countPrimes(self,n):
        if n < 3:
            return 0
        else:
            new_list = [1] * n
            new_list[0],new_list[1] = 0,0
            for i in range(2,int(n**0.5)+1):
                if new_list[i]:
                    new_list[i*i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(new_list)
my = Solution()
print(my.countPrimes(99998))