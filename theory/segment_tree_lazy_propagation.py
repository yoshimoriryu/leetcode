class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, data)
        print(self.tree)

    def build(self, node, l, r, data):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(node * 2, l, mid, data)
            self.build(node * 2 + 1, mid + 1, r, data)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
        print(self.tree, l, r)

    def push(self, node, l, r):
        """ Apply and propagate lazy value down to children """
        if self.lazy[node] != 0:
            self.tree[node] += (r - l + 1) * self.lazy[node]
            if l != r:  # not a leaf node
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node, l, r, i, j, val):
        self.push(node, l, r)
        if r < i or l > j:
            return
        if i <= l and r <= j:
            self.lazy[node] += val
            self.push(node, l, r)
            return
        mid = (l + r) // 2
        self.update_range(node * 2, l, mid, i, j, val)
        self.update_range(node * 2 + 1, mid + 1, r, i, j, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query_range(self, node, l, r, i, j):
        self.push(node, l, r)
        if r < i or l > j:
            return 0
        if i <= l and r <= j:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query_range(node * 2, l, mid, i, j)
        right = self.query_range(node * 2 + 1, mid + 1, r, i, j)
        return left + right

    def update(self, i, j, val):
        self.update_range(1, 0, self.n - 1, i, j, val)

    def query(self, i, j):
        return self.query_range(1, 0, self.n - 1, i, j)

data = [1, 2, 3, 4, 5, 6, 7, 8]
st = SegmentTree(data)

print(st.query(0, 7))  # 36

st.update(2, 5, 10)  # Add +10 to indices 2 through 5

print(st.query(0, 7))  # Now should be 36 + (10*4) = 76
print(st.query(2, 5))  # Just the updated part: 3+4+5+6 + 10*4 = 58
