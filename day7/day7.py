with open("day7/day7.in.txt") as input:
    crabs =  [int(crab) for crab in [(line.split(',')) for line in input][0]]
print(crabs)
sumofcrabs = sum(crabs)
least_fuel = 10000000000
best_position = -1
for target in range(max(crabs)+1):
    fuel = 0
    for crab in crabs:
        
        m, n = crab, target
        if m > n:
            m, n = n, m 
        m, n = (m-m+1), n-m+1
        crab_fuel = sum(range(m,n))
        fuel += crab_fuel
    if(fuel < least_fuel):
        print('new record {}'.format(least_fuel))
        least_fuel , best_position= fuel, target
  
print(least_fuel)
print(best_position)
