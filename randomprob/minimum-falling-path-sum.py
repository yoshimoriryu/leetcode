# failed to solve
class Solution(object):
	def minFallingPathSum(self, arr):
		for i in range(1,len(arr)):
			for j in range(len(arr[0])):
				print(arr)
				if j==0:
					arr[i][j] += min([arr[i-1][j+1], arr[i-1][j]])
				elif j==len(arr[0])-1:
					arr[i][j] += min([arr[i-1][j-1], arr[i-1][j]])
				else:
					arr[i][j] += min([arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1]])
		return min(arr[-1])

arr = [[2,1,3],[6,5,4],[7,8,9]]
x = Solution()
print(x.minFallingPathSum(arr))