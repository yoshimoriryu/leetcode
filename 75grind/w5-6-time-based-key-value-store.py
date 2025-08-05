from collections import defaultdict


# long runtime 945 ms
class TimeMap:
    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.timemap[key]:
            self.timemap[key].append((value,timestamp))
        else:
            bisect.insort(self.timemap[key],(value,timestamp), key=lambda x: -x[1])
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.timemap[key]
        for val,ts in val:
            if ts <= timestamp:
                return val
        return ""

#### solution; 483 ms
class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)