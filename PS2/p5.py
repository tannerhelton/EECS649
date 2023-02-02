slist = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
TIME = len(slist)
a = 0
b = 0
print("t, s, a, b")
for t in range(TIME):
    s = slist[t]
    print(t, s, a, b)
    # compute these all "in parallel"; if placed one after the other, results are wrong
    a, b = map(int,(s+a>=1, s+a+b>=2))