from pprint import pprint

def bfs(grid, o):
    R, C = len(grid), len(grid[0])

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [-1, -1], [1, 1], [-1, 1]] # diagonal movements allowed
    lives = [[-1 for j in range(C)] for i in range(R)]

    q = []

    q.append([0, 0, o, 0]) # row, col, lives, distance

    log = []

    # use for later to tag used step
    turn = 0
    batch = []

    while len(q):
        #get next step
        cr, cc, clives, cdist = q.pop(0)

        # return when reached the end
        if cr == R - 1 and cc == C - 1:
            return log

        # remove one life/obstacle
        if grid[cr][cc] == 1:
            clives -= 1

        # push potential movements to queue
        for d in directions:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < R and 0 <= nc < C and lives[nr][nc] < clives:
                q.append([nr, nc, clives, cdist + 1])
                lives[nr][nc] = clives

        # push to log
        log.append([cr, cc, clives, cdist])

    # if no path possible to end
    return -1

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

numberOfRemovableObstacles = 1

log = bfs(grid, numberOfRemovableObstacles)

pprint(log)
