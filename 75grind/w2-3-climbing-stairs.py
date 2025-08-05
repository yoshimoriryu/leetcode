
# soal ini fibonacci
# read discussion
class Solution:
    def climbStairs(self, n: int) -> int:
        f = {}
        f[1] = 1
        f[2] = 2
        i = 3
        while i <= n:
            print(i)
            f[i] = f[i-1] + f[i-2]
            print(f[i])
            i += 1
        print(f)
        return f[n]

    def printAnswer(self, answer):
            print(answer)

if __name__ == "__main__":
    n = 2
    x = Solution()
    x.printAnswer(x.climbStairs(n))
    

