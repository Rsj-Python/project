class Solution():
    def myAtoi(self,s):
        new_s = '+-0123456789'
        s = s.strip()
        for i in range(len(s)):
            if s[i] not in new_s:
                try:
                    new_int = int(float(s[0:i]))
                except:
                    return 0
                if new_int < -2**31:
                    return -2**31
                elif new_int > 2**31-1:
                    return 2**31-1
                else:
                    return new_int
            elif i == len(s)-1:
                try:
                    new_int = int(float(s[0:]))
                except:
                    return 0
                if new_int < -2**31:
                    return -2**31
                elif new_int > 2**31-1:
                    return 2**31-1
                else:
                    return new_int
            elif s[i] in new_s[2:] and (s[i+1] == '-' or s[i+1] =='+'):
                try:
                    new_int = int(float(s[0:i+1]))
                except:
                    return 0
                if new_int < -2**31:
                    return -2**31
                elif new_int > 2**31-1:
                    return 2**31-1
                else:
                    return new_int
        if s == '':
            return 0
        # elif int(float(s)) < -2**31:
        #     return -2**31
        # else:
        #     return int(float(s))
my = Solution()
print(my.myAtoi("-5-"))
