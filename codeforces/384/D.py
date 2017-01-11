import sys

lines = sys.stdin.read().splitlines()
N = int(lines[0])

if N == 1:
    print "Impossible"
    sys.exit(0)

score = [int(x) for x in lines[1].split(" ")]

connected = {}
for i in range(N-1):
    l, r = [int(x) - 1 for x in lines[2 + i].split(" ")]
    if l not in connected:
        connected[l] = set()
    if r not in connected:
        connected[r] = set()
    connected[l].add(r)
    connected[r].add(l)

tree = {}
visited = [False] * N
def bfs(node):
    global connected, visited
    visited[node] = True
    if node not in tree:
        tree[node] = set()
    for child in connected[node]:
        if visited[child] == False:
            tree[node].add(child)
            bfs(child)

bfs(0)

best = - 10**9 - 1
chosen = False

def dfs(node):
    global tree, best, chosen
    if len(tree[node]) == 0:
        # print node, score[node], score[node]
        return score[node], score[node]

    if len(tree[node]) > 1:
        chosen = True

    total = score[node]
    bests = []
    for child in tree[node]:
        s, cbest = dfs(child)
        total += s
        bests.append(cbest)

    bests = sorted(bests)
    if len(bests) >= 2:
        cbest = bests[-2] + bests[-1]
        if cbest > best:
            best = cbest

    if total > bests[-1]:
        # print node, total, total
        return total, total
    # print node, total, bests[-1]
    return total, bests[-1]

s, cbest = dfs(0)
if s > best:
    best = s
if cbest > best:
    best = cbest

if chosen:
    print best
else:
    print "Impossible"
