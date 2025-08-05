from typing import List
from collections import defaultdict

# SOLVED TAPI BAPUK COK, jadi:
# failed to solve
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        for acc in accounts:
            acc_emails = acc[1:]
            if acc[0] not in d:
                d[acc[0]].append(sorted(set(acc_emails)))
            else:
                len_acc = len(set(acc_emails))
                is_len_change = False
                for idx, listed_acc in enumerate(d[acc[0]]):
                    is_len_change = len_acc - len(set(acc_emails) - set(listed_acc))
                    # same account
                    if is_len_change:
                        listed_acc = sorted(set(acc_emails).union(set(listed_acc)))
                        d[acc[0]][idx] = listed_acc
                        break
                # diff account
                if not is_len_change:
                    d[acc[0]].append(sorted(set(acc_emails)))

        res = []
        last_email = ''
        for k,v in d.items():
            # for each name, merge every list that has same email
            i, n = 0, len(v)
            while i < n:
                acc = v[i]
                is_merge = False
                for email in acc:
                    if i + 1 < n:
                        j = i + 1
                        while j < n:
                            curr_len = len(v[i])
                            diff_len = len(set(v[i]) - set(v[j]))
                            if curr_len != diff_len:
                                is_merge = True
                                v[i] = sorted(list(set(v[i] + v[j])))
                                v.remove(v[j])
                                n -= 1
                            else:
                                j += 1

                if is_merge: i = i
                else: i += 1

            for acc in v:
                x = [k]
                x.extend(acc)
                res.append(x)
        return res


# SOLUTION: union find
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]