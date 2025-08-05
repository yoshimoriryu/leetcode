class Solution:
    # mine, ori
    def addBinary(self, a: str, b: str) -> str:
        c2 = '1111'
        c,c2 = self.addTwoBinary(a,b)
        while not self.isAllZero(c2):
            if self.isAllZero(c):
                return c2

            while c2[:1] == '0':
                c2 = c2[1:]
            c, c2 = self.addTwoBinary(c,c2)
        return c

    def isAllZero(self, s):
        y = s
        y = y.replace('0','')
        if y == '':
            return True
        else:
            return False
    
    def addTwoBinary(self, s1, s2):
        if self.isAllZero(s1) and self.isAllZero(s2):
            return '0','0'
        lens1 = len(s1)
        lens2 = len(s2)
        c = ''
        c2 = '0'
        n = max(lens1, lens2)
        for i in range(n):
            remain = ''
            lens1 = len(s1)
            lens2 = len(s2)
            char1 = s1[lens1-1:]
            char2 = s2[lens2-1:]
            if char1 == char2:
                if char1 == '1':
                    remain = '1'
                c = '0' + c
            else:
                if char1 > char2:
                    c = char1 + c
                else:
                    c = char2 + c

            if remain:
                c2 = remain + c2
            else:
                c2 = '0' + c2
            s1 = s1[:-1]
            s2 = s2[:-1]
        return c,c2

    # PY solution (idk good or no)
    def addBinary2(self, a:str, b: str) ->str:
        return bin(int('0b'+a,2) + int('0b'+b,2))[2:]
    
    # PY better readable, spec approved
    def addBinary3(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        print(a, b)
        while i >= 0 or j >= 0 or carry:
            print(i, j, carry, s)
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    a = '11'
    b = '11'
    x = Solution()
    x.printAnswer(x.addBinary3(a,b))
