# 1.面包师好代码版
def cakes(recipe, available):
    return min(available.get(k,0) // recipe[k] for k in recipe)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe,available))
# 2.全排列(字符串)好代码版
import itertools as per
def permutations(string):
    return ["".join(str) for str in set(per.permutations(string))]
print(permutations('abcd'))

# 3.double colas(双可乐)好代码版(这个是神一般的解法，表示看不懂)
def who_is_next(names, r):
    while r > len(names):
        r = (r - (len(names)-1)) // 2
    return names[r-1]
names = ["Sheldon", "Leonard","Penny", "Rajesh", "Howard"]
print(who_is_next(names,100))

# 4.计算重复次数好代码版
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])
print(duplicate_count('aAbbcc'))
# 5.有效扩号好代码版
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
            if count < 0:
                return count
    return count == 0
print(valid_parentheses('())((())()'))
# 6.字符串增量好代码版
def increment_string(strng):
    head = strng.rstrip('0123456789')  # 删除 string 字符串末尾的指定字符（默认为空格）. '0123456789' 就是删除在0123456789中的值  只要有就删除
    tail = strng[len(head):]  # 从头的结尾处开始取到最后 就是把后面的数字串取出来
    if tail == '':
        return head + '1'
    return head + str(int(tail) + 1).zfill(len(tail))  # zfill方法返回指定长度的字符串（括号内为指定长度），原字符串右对齐，字符串长度不够，在字符串前面填充0。
increment_string("foo002")

# 7.Strings Mix(字符串混合)好代码版
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x:hist[x]))
print(mix('Are they here', 'yes, they are here'))

# 8.选择峰(Pick peaks)好代码版
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prob_peak = i
        elif arr[i] < arr[i - 1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}
# 9.正方形的周长好代码版
def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)
# 10.斐波那契数列好代码版
def fib(n):
    # return n if n < 2 else fib(n-1) + fib(n-2)
    one,two = 0,1
    print('f(0)=',one)
    for i in range(0,n):
        one = one + two
        two = one - two
        print('f(%s)='%(i+1),one)
fib(100)
