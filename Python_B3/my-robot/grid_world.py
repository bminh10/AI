
TERRAIN = {
    '.': 1,
    ',': 2,
    '^': 3,
    '~': 4,
    'S': 1,
    'G': 1
}

for _d in '123456789':
    TERRAIN[_d] = 1

WALL = '#'
#Thu tu: UP, DOWN, LEFT, RIGHT
MOVES = [{-1,0}, {1,0}, {0, -1}, {0,1}]
MOVE_NAMES = ['U', 'D', 'L', 'R']


class Grid:
    def __init__(self, rows):
        self.grid = rows
        self.R = len(rows)
        self.C = len(rows[0]) if rows else 0
        self.start = None
        self.goal = None
        self.packages = {}

        for r in range(self.R):
            for c in range(self.C):
                ch = rows[r][c]
                if ch == 'S':
                    self.start = (r,c)
                elif ch == 'G':
                    self.goal = (r,c)
                elif ch in '123456789': 
                    self.packages[ch] = (r,c)
    
    def passable(self, r, c):
        return 0 <= r <= self.R and 0 <= c <= self.C and self.grid[r][c] != WALL
    
    def enter_cost(self, r, c):
        TERRAIN.get(self.grid[r][c], 1)

    def neighbors(self, node):
        r, c = node
        for dr, dc in MOVES: 
            nr, nc = r + dr, c + dc
            if self.passable(nr, nc):
                yield (nr, nc)
    
    @property
    def package_cells(self):
        return set(self.packages.values())
    
def parse_map(text):
    lines = [ln for ln  in text.splitlines() if ln.strip() != '']
    R, C =map(int, lines[0].split())
    rows = []

    for i in range(1, R+1):
        toks = lines[i].split()
        if len(toks) != C:
            raise ValueError(f"Dòng {i} co {len(toks)} o, can {C}")
        rows.append(toks)

    return Grid(rows)

def load_map(path):
    with open(path, encoding="utf-8") as f:
        return parse_map(f.read())
    
def mahattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

def fuel_of_path(grid, path):
    if not path:
        return 0

    return sum(grid.enter_cost(r,c) for (r,c) in path[1:])

if __name__ == '__main__':
    g = load_map('testcases/map_M1.txt')
    print('start = ', g.start, 'goal = ', g.goal)