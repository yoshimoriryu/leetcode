class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = {}
        for i in magazine:
            if i in m_dict:
                m_dict[i] += 1
            else:
                m_dict[i] = 1
        
        for i in ransomNote:
            print(i)
            if i in m_dict:
                m_dict[i] -= 1
                if m_dict[i] < 0:
                    return False
            else:
                return False
        return True

    # set punya elmt.count (built-in)
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        t = set(ransomNote)
        for i in t:
            if ransomNote.count(i) > magazine.count(i) or i not in magazine:
                return False
        return True

    def printAnswer(self, answer):
            print(answer)

if __name__ == "__main__":
    a = 'apalu'
    b = 'apalu'
    x = Solution()
    x.printAnswer(x.canConstruct(a, b))
    

