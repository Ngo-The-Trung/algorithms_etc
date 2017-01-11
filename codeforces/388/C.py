import sys

lines = sys.stdin.read().splitlines()
N = n = int(lines[0])

a = [v for v in lines[1]]


D = R = D_ = R_ = 0
while True:
    D = R = 0
    for i in range(N):
        # print a[i], R_, D_, R, D
        if a[i] == 'D':
            if R_ > 0:
                a[i] = ' '
                R_ -= 1
            else:
                D += 1
                D_ += 1
        elif a[i] == 'R':
            if D_ > 0:
                a[i] = ' '
                D_ -= 1
            else:
                R += 1
                R_ += 1
    n = D + R
    # print a, D, R, D_, R_
    if R == 0:
        print "D"
        break
    elif D == 0:
        print "R"
        break
