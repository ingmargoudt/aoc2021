with open('day9/day9.txt') as input:
    heights = [list(map(int, list(digit.strip()))) for digit in input]
print(heights)
lowpoints = []
used = set()
basins = []
for y in range(0,len(heights)):
    for x in range(0, len(heights[y])):
        if((y,x) in used or heights[y][x] == 9):
            continue
        
        basin = []
        worklist = []
        basin.append((y,x))
        worklist.append((y,x))

        while worklist:
            pivot = worklist.pop();
            if pivot in used:
                continue
            else:
                used.add(pivot)
            yy, xx = pivot[0], pivot[1];
            theValue = heights[pivot[0]][pivot[1]]
            neighbours = set()
            ly, lx = yy, xx-1
            uy, ux = yy-1, xx
            ry, rx = yy, xx+1
            dy, dx = yy+1, xx
            if(lx>=0):
                neighbours.add((ly,lx))
            if(uy>=0):
                neighbours.add((uy,ux))
            if(rx<len(heights[0])):
                neighbours.add((ry, rx))
            if(dy<len(heights)):
                neighbours.add((dy,dx))
            
            for nb in neighbours:
                if(heights[nb[0]][nb[1]]) < 9 and nb not in used and nb not in basin:
                    basin.append(nb)
                    #print("adding "+str(nb))
                    worklist.append(nb)
        print("basin: " +str(basin) + " len: "+str(len(basin)))
        if len(basin)>0:
            basins.append(len(basin))
basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])