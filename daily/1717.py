class Solution:
    def maximumGain1(self, s: str, x: int, y: int) -> int:
        # TLE BANG AAZZZZ
        # xs = "ab"
        # ys = "ba"
        # p1_score = x if max(x,y) == x else y
        # p1_str = xs if max(x,y) == x else ys
        # p2_score = x if min(x,y) == x else y
        # p2_str = xs if min(x,y) == x else ys
        # score = 0

        # while True:
        #     flag1 = False
        #     flag2 = False
        #     #scan for prio1
        #     i = -2
        #     count1 = 0
        #     while i != -1:
        #         i = s.find(p1_str)
        #         if i != -1:
        #             count1 += 1
        #             s = s.replace(p1_str, "", 1)
        #             flag1 = True
        #     score += count1*p1_score

        #     #scan for prio2
        #     j = -2
        #     count2 = 0
        #     while j != -1:
        #         j = s.find(p2_str)
        #         if j != -1:
        #             count2 += 1
        #             s = s.replace(p2_str, "", 1)
        #             flag2 = True
        #     score += count2*p2_score
        #     if not flag1 and not flag2:
        #         break
        # return score
        pass
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) == 1:
            return 0

        xs = "ab"
        ys = "ba"
        p1_score = x if max(x,y) == x else y
        p1_str = xs if max(x,y) == x else ys
        p2_score = x if min(x,y) == x else y
        p2_str = xs if min(x,y) == x else ys
        score = 0
        stack = [s[0]]

        if x == y:
            p1_score = x
            p1_str = xs
            p2_score = y
            p2_str = ys

        i = 1
        while i < len(s):
            # print(i, stack, score, p1_str)
            if stack:
                sub = stack[-1] + s[i]
                if sub == p1_str:
                    score += p1_score
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1

        if stack:
            j = 1
            stack2 = [stack[0]]
            while j < len(stack):
                # print(j, stack2, score, p2_str)
                if stack2:
                    sub = stack2[-1] + stack[j]
                    if sub == p2_str:
                        score += p2_score
                        stack2.pop()
                    else:
                        stack2.append(stack[j])
                else:
                    stack2.append(stack[j])
                j += 1
        return score
            


s = "cdbcbbaaabab"
x = 4
y = 4
z = Solution()
print(z.maximumGain(s,x,y))        