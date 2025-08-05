from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i = 0
        n = len(bank)
        beam_count = 0
        while i < n:
            if "1" in bank[i]:
                i_count = bank[i].count("1")
                j = i + 1
                j_count = 0
                while j < n:
                    print(j)
                    if "1" in bank[j]:
                        j_count = bank[j].count("1")
                        break
                    j += 1
                beam_count = beam_count + i_count*j_count
            i = j if j > i else i+1
        return beam_count

bank = ["011001","000000","010100","001000"]
x = Solution()
print('number of laser', x.numberOfBeams(bank))