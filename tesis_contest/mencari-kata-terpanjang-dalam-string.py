import sys

def your_answer(line):
    line = line.split()
    N = len(line)
    longest = (-1,0) # idx, long
    for i in range(N):
        l = len(line[i])
        if l > longest[0]:
            longest = (l, i)
        # print(longest, line[i])
    return line[longest[1]]
    # your answer here


for line in sys.stdin:
    line = line.strip()

    print(your_answer(line))
# line = "the quick brown fox"
# print(your_answer(line))