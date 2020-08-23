class Solution():
    def fizzBuzz(self,n):
        new_list = ['1','2']
        for i in range(3,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                new_list.append('FizzBuzz')
            elif i % 3 == 0:
                new_list.append('Fizz')
            elif i % 5 == 0:
                new_list.append('Buzz')
            else:
                new_list.append(str(i))
        return new_list[0:n]
my = Solution()
print(my.fizzBuzz(15))