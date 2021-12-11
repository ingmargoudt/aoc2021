with open('day8/day8.in.txt') as input:
    digits = [digit.split('|')[1].split(' ') for digit in input]

#print(digits)
occurences = 0
for l in digits:
    #print(l)
    for e in l:
        e=len(e.split('\n')[0])
        if e in (2,3,4,6):
            #print('y')
            occurences += 1
print(occurences)