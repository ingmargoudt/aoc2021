with open("day6/day6.in.txt") as input:
        p =  [int(p) for p in [(line.split(',')) for line in input][0]]
        population = {x:p.count(x) for x in p}
DAYS = 256
currentday = 0
while currentday < DAYS:
    new_population = dict.fromkeys(list(range(0,8)), 0)
    for state, amount in population.items():
        if(state == 0):
            new_population[6] += amount
            new_population[8] = amount
        else:
            new_population[state-1] += amount
    population = new_population
    currentday+=1
    print(sum(population.values()))
    #print('After {} day{}: {}'.format(currentday, 's' if currentday > 1 else '',new_population))