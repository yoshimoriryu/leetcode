class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = {}
        td = {}
        for i in s:
            if i in sd:
                sd[i] += 1
            else:
                sd[i] = 1

        for i in t:
            if i in td:
                td[i] += 1
            else:
                td[i] = 1

        reserve = {}
        count = 0
        reserve = False
        for k,v in td.items():
            if k in td and k in sd:
                if td[k] != sd[k]:
                    td[k] = td[k] - sd[k]
                    if td[k] < 0:
                        count = count - td[k]
                else:
                    td[k] = 0
            else:
                reserve = True

        if reserve:
            t_sum = sum(td.values())
            count = count + t_sum
        return count

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    s = 'leetcode'
    t = 'practice'
    x = Solution()
    print(s,t)
    x.printAnswer(x.minSteps(s, t))
    

