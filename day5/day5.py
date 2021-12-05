from os import linesep
import math

def day5():
    with open("day5/day5.in.txt") as input:
        lines = [list(map(int, i)) for i in [c.split(',') for c in [line.replace('->',',') for line in [line.strip() for line in input]]]]
    x = max(max([l for l in lines]))
    print(x)
    m = [[0 for a in range(x+2)] for b in range(x+2)]
    for instruction in lines:
        x1, y1, x2, y2 = instruction
        print(instruction)
        
        xrange = range(x1, x2+(1 if x2 > x1 else -1), -1 if x2 < x1 else 1)
        yrange = range(y1, y2+(1 if y2 > y1 else -1), -1 if y2 < y1 else 1)
        if x1 == x2:
            for dy in yrange:
                m[dy][x1] = m[dy][x1]+1
        elif y1 == y2:
            for dx in xrange:
                m[y1][dx] = m[y1][dx]+1
        
        elif abs(x1 - x2) == abs(y1 - y2):
            xcursor, ycursor = x1, y1
            stop = False
            while(not stop):
                m[ycursor][xcursor] = m[ycursor][xcursor]+1
                xcursor += -1 if x2 < x1 else 1
                ycursor += -1 if y2 < y1 else 1
                stop = xcursor == x2 and ycursor == y2
            m[ycursor][xcursor] = m[ycursor][xcursor]+1
        else:
            print('no idea')
    p = len([x for x in sum(m, []) if x > 1])
    print(p, end = '\n')
    
day5()