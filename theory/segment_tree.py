class SegmentTree:
    def __init__(self, data, tree_type):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.tree_type = tree_type
        print("Init Tree: ", self.n, self.tree)
        # Build tree sum
        if tree_type == 0:
            for i in range(self.n):
                self.tree[self.n + i] = data[i]
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        # Build tree max
        elif tree_type == 1:
            for i in range(self.n):
                self.tree[self.n + i] = data[i]
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
        print(self.tree)

    def update(self, index, value):
        print("Update", index, value)
        # Set value at leaf node
        i = index + self.n
        self.tree[i] = value
        # Update parents
        if self.tree_type == 0:
            while i > 1:
                print(i, self.tree)
                i //= 2
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        elif self.tree_type == 1:
            while i > 1:
                self.tree[i] = max(self.tree[2 * 1], self.tree[2 * 1 + 1])
        print(i, self.tree)

    def findout_in_range(self, left, right):
        # Sum from index `left` to `right` inclusive
        print("findout_in_range ", left, right)
        print(arr)
        result = 0
        l, r = left + self.n, right + self.n + 1
        if self.tree_type == 0:
            while l < r:
                print(result, l, r)
                if l % 2 == 1:
                    result += self.tree[l]
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    result += self.tree[r]
                l //= 2
                r //= 2
        elif self.tree_type == 1:
            while l < r:
                print(result, l, r)
                if l % 2 == 1:
                    result = self.tree[l]
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    result = self.tree[r]
                l //= 2
                r //= 2
        return result

    def print_tree(self):
        level = 0
        i = 1
        total_nodes = 2 * self.n
        print("Segment Tree Structure:")
        while i < total_nodes:
            num_nodes = 2 ** level
            nodes = self.tree[i:i + num_nodes]
            print(f"Level {level}: {nodes}")
            i += num_nodes
            level += 1

    def print_tree2(self):
        def dfs(index, indent=""):
            if index >= 2 * self.n:
                return
            if index >= self.n:
                print(f"{indent}└── [Leaf {index - self.n}] {self.tree[index]}")
                return
            print(f"{indent}└── {self.tree[index]}")
            dfs(2 * index, indent + "    ")
            dfs(2 * index + 1, indent + "    ")

        print("Segment Tree (as binary tree):")
        dfs(1)


arr = [1, 3, 5, 7, 9, 11]
print(arr)
st = SegmentTree(arr, 0)
sts = SegmentTree(arr, 1)
print(" here ")
print(sts.findout_in_range(1, 3))
# st.print_tree()
# st.print_tree2()

# print(st.findout_in_range(1, 3))  # Output: 15 (3+5+7)
# st.update(2, 6)            # Change arr[2] = 6
# print(st.findout_in_range(1, 3))  # Output: 16 (3+6+7)

# st.print_tree()
# st.print_tree2()