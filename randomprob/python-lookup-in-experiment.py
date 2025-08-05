import sys, time

mylist = []
myset = set()
mydict = {}
start = time.time()
for i in range(9999999):
    mylist.append(i)
    myset.add(i)
    mydict[i] = i

end = time.time()
print('elapsed', end-start)

start = time.time()
if i/2 in mylist:
    print('list', i)
    end = time.time()
    print('list', end-start)

start = time.time()
if i/2 in mylist:
    print('dict', i)
    end = time.time()
    print('dict', end-start)

start = time.time()
if i/2 in myset:
    print('set', i)
    end = time.time()
    print('set', end-start)
