from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        newInterval = intervals[0]
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            print(newInterval, result)
        result.append(newInterval)
        return result

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
x = Solution()
print(x.merge(intervals))