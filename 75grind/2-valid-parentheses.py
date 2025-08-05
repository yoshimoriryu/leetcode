class Solution:

    # Time O(n), space O(n)
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 == 1:
            return False
        
        h = s[0]
        t = s[1:]
        while True:
            # print("===")
            # print(h)
            # print(t)
            if t:
                if h[len(h)-1:] == '(' and t[0] == ')':
                    h = h[:len(h)-1]
                    t = t[1:]
                elif h[len(h)-1:] == '{' and t[0] == '}':
                    h = h[:len(h)-1]
                    t = t[1:]
                elif h[len(h)-1:] == '[' and t[0] == ']':
                    h = h[:len(h)-1]
                    t = t[1:]
                else:
                    if t:
                        h = h + t[0]
                        t = t[1:]
                    else:
                        break
            else:
                break
        if not h and not t:
            return True
        else:
            return False

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    s = "(("
    x = Solution()
    x.printAnswer(x.isValid(s))

