# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_anc_dict = {}
        q_anc_dict = {}
    
        self.search(root, p, p_anc_dict, 0)
        self.search(root, q, q_anc_dict, 0)

        i, j = len(p_anc_dict), len(q_anc_dict)
        # for key, value in p_anc_dict.items():
        #     print(key, value.val)
        # for key, value in q_anc_dict.items():
        #     print(key, value.val)
        idx = min(i,j)
        k = 0
        lca = root
        while k < idx:
            if (p_anc_dict[k] == q_anc_dict[k]):
                lca = p_anc_dict[k]
            else:
                break
            k +=1
        return lca

    # Recursive search
    def search(self, root, p, ancestor_list, depth):
        ancestor_list[depth] = root
        if root.val == p.val:
            depth += 1
            return
        elif p.val > root.val:
            depth += 1
            return self.search(root.right, p, ancestor_list, depth)
        elif p.val < root.val:
            depth += 1
            return self.search(root.left, p, ancestor_list, depth)