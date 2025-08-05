from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        track_count = defaultdict(list) # count: [list of number with 'count' occurence]
        track_number = {}
        for num in arr:
            print(num)
            print(track_number)
            print(track_count)
            if num in track_number:
                track_count[track_number[num]].remove(num)
                track_number[num] += 1
                track_count[track_number[num]].append(num)
            else:
                track_number[num] = 1
                track_count[1].append(num)

        for k,v in track_count.items():
            if len(v) > 1:
                return False
        return True

arr = [1,2,2,1,1,3]
x = Solution()
print(x.uniqueOccurrences(arr   ))