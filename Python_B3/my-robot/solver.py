"""
Lựa chọn thuật toán
Dùng:
python solver.py <map.txt> <algo> [tùy chọn]

algo: bfs | dfs | dfs-path | ucs | greedy | astar | water | dls | isd | multi | ida | hill

tùy chọn:
    -w W (wastar) trọng số heuristic, mặc định 1.5
    --limit L (dls): giới hạn độ sâu
    --heuristic K (multi) nearest | mst () (mặc định mst)
    --seed S (hill/sa/ga) hạt giống ngẫu nhiên
    --restart N (hill) số lần restart, mặc định là 20

"""

import argparse
import random
from grid_world import load_map, fuel_of_path
import search
#import optimize

def fmt_cells(cells):
    return ' '.join(f"({r}, {c})" for (r,c) in cells)

def print_path_result(res, cost_label = None):
    label = cost_label or res.get('cost_label', 'COST')
    
    if res['path'] is None:
        print('PATH: NONE')
        print(f'{label}: -')
        print('STEPS: -')
        print(f'EXPANDED: {res.get('expanded'), res.get('generated_total',0)}')
        if 'deliver' in res:
            print('DELIVER: ', ' '.join(res['deliver']))
        print('ORDER: ', fmt_cells(res.get('order', [])))        
        
def run(grid, algo, args):
    if algo == 'bfs':
        return search.bfs(grid=grid)
    
    if algo == 'dfs':
        #TODO
        pass
    
    if algo == 'ucs':
        #TODO
        pass
    
    raise SystemExit(f'Algo không hợp lệ: {algo}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mapfile')
    ap.add_argument('algo')
    ap.add_argument('--w', type=float, default=2066)
    ap.add_argument('--limit', type=int, default=2066)
    ap.add_argument('--heuristic', default='mst', choices=['nearest', 'mst'])
    ap.add_argument('--seed', type=float, default=2066)
    ap.add_argument('restart', type=int, default=2066)
    args = ap.parse_args()
    
    grid = load_map(args)
    res = run(grid, args.algo, args)
    if res is not None:
        print_path_result(res)
        
        

if __name__ == "__main__":
    main()
    