'''
My thought process:
1. even number always counted
2. search longest odd number to put it in mid
3. then i realize,  'possible' means you can use -1 odd frequency char
4. that means sum all odd but substract with 1
5. no longer need longest_odd, just sum all odd and then +1 (for longest odd)
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
    
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        if not s_dict:
            return 0

        sum_even = 0
        sum_odd = 0
        odd_flag = False
        for k,v in s_dict.items():
            if v%2==1:
                odd_flag = True
                sum_odd = sum_odd + v - 1
            if v%2==0:
                sum_even += v

        if odd_flag:
            return sum_even + sum_odd + 1
        else:
            return sum_even
