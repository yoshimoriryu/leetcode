# your code goes here
line = input()
import collections

def your_answer(line):
    # d = collections.defaultdict(int)
    # for el in line:
    #     d[el] += 1
    # return d
    return collections.Counter(line)
answer = your_answer(line)
answer_arr = []

for key, value in answer.items():
    answer_arr.append(f"{key}: {value}")

print("{ " + (", ".join(answer_arr)) + " }")