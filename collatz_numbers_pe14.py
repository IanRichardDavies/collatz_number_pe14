# my solution for problem 14
# finds the number from 1 up to n that produces the longest Collatz number sequence

def memoize(function):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = function(x)
        return cache[x]
    return helper
        
@memoize
def collatz(n):
    max = [0,0]
    for num in range(2, n+1):   
        possible = num
        counter = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                counter += 1
            else:
                num = 3*num + 1
                counter += 1
        if counter > max[0]:
            max[0] = counter
            max[1] = possible
    return max
                            
collatz(1000000)