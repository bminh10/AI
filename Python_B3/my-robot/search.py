import heapq
from collections import deque
from grid_world import mahattan, reconstruct, fuel_of_path


# L1: BFS
def bfs(grid):
    start, goal = grid.start, grid.goal
    frontier = deque([start])
    parent = {start: None}
    order = []

    while frontier:
        cur = frontier.popleft()
        order.append(cur)

        if cur == goal:
            path = reconstruct(parent, cur)
            return {
                "path": len(path),
                
                "cost": len(path) - 1,
                "steps": len(path) - 1,
                "expanded": len(order),
                "older": order,
                "cost_label": "STEPS",
            }

        for nb in grid.neighbors(cur):
            if nb not in parent:
                parent[nb] = cur
                frontier.append(nb)

    return {
        "path": None,
        "cost": None,
        "steps": None,
        "expanded": len(order),
        "older": order,
        "cost_label": "STEPS",
    }


if __name__ == "__main__":
    from grid_world import load_map

    g = load_map("testcases/map_M1.txt")
    r = bfs(g)
    print(f"bfs step = {r['steps']} path = {r['path']}")
