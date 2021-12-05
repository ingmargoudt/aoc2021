with open("day1.in.txt") as input:
    depths = [int(line.strip()) for line in input]

depth_increase = 0
for i in range(1, len(depths)-2):
    if sum(depths[i:i+3]) > sum(depths[i - 1:i-1+3]):
        print(str(sum(depths[i:i+3])) + " increased")
        depth_increase +=1
    else:
        print(str(sum(depths[i:i+3])))

print(depth_increase)