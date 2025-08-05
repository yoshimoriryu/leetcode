
# failed to solve, TLE
class Solution:
    def dailyTemperatures(self, T):
        #initialize the result array with all '0's considering when there is no bigger temperature
        ans = [0]*len(T) 
        stack = []
        
        for i,v in enumerate(T):
            #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
            count = 0
            while stack and stack[-1][1] < v:
                count += 1
                print(count)
                index,value = stack.pop()
                ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
            #Remember since we are comparing all the stack elements before inserting,all the stack elements will have temperatures greater than the current value	
            stack.append([i,v])      
        
        return ans
        
        #Happy Coding


# short one
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lower = stack.pop()
                ret[lower[1]] = i - lower[1]
            stack.append((temp,i))
        return ret