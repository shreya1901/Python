import math
# Returns the lcm of first n numbers
def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans * i)/math.gcd(ans, i))
    return ans
# main
n = int(input('Enter maximum limit n : '))
print (lcm(n))
