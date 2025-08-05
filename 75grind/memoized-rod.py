import sys
 
# A utility function to get the
# maximum of two integers
def max(a, b):
    return a if (a > b) else b
     
# Returns the best obtainable price for a rod of length n 
# and price[] as prices of different pieces
def cutRod(price, n):
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1
     
    # Recursively cut the rod in different pieces  
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val

INT_MIN = -32767

def cutRodMemoized(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0
 
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        print('ini I', i)
        max_val = INT_MIN
        for j in range(i):
             print('ini jjjjj', j)
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
        print(val)
 
    return val[n]

# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20] # price
size = len(arr)
print("Maximum Obtainable Value is", cutRodMemoized(arr, size))