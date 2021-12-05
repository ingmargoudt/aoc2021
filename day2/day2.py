with open("day2.in.txt") as input:
    instructions = [(line.strip()) for line in input]
horizontal = 0
depth = 0
aim = 0
for inst in instructions:
    operand, value = inst.split(' ')

    if(operand == 'forward'):
        horizontal += int(value)
        depth += aim * int(value)
    elif(operand == 'up'):
        aim -= int(value)
    elif(operand == 'down'):
        aim += int(value)
        
print(horizontal)
print(depth)
print(horizontal * depth)
