class SegmentTree:
    def __init__(self, data, operation, default):
        self.n = len(data)
        self.tree = [default] * (2 * self.n)
        self.operation = operation
        self.default = default
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.operation(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.operation(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, l, r):
        res = self.default
        l += self.n
        r += self.n + 1
        while l < r:
            if l % 2 == 1:
                res = self.operation(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.operation(res, self.tree[r])
            l //= 2
            r //= 2
        return res

# Sum Segment Tree
sum_tree = SegmentTree([1, 3, 5, 7, 9, 11], operation=lambda a, b: a + b, default=0)

# Max Segment Tree
max_tree = SegmentTree([1, 3, 5, 7, 9, 11], operation=max, default=float('-inf'))

# Min Segment Tree
min_tree = SegmentTree([1, 3, 5, 7, 9, 11], operation=min, default=float('inf'))
