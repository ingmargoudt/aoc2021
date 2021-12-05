with open("day3.in.txt") as input:
    diagnostic_report = [line.strip() for line in input]
oxygen = ''
co2 = ''
print(diagnostic_report)
base = diagnostic_report
for i in range(0, len(diagnostic_report[0])):
    zero_count = 0;
    one_count = 0
    occurences = {}
    diagnostic_report = [x for x in diagnostic_report if x.startswith(oxygen)]
    if(len(diagnostic_report) == 1):
        oxygen = diagnostic_report[0]
        break
    for measurement in diagnostic_report:
        if(measurement[i] == '0'):
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        oxygen += '0'
        #co2 += '1'
    else:
        oxygen += '1'
        #co2 += '0'
diagnostic_report = base
zero_count = 0
one_count = 0
for i in range(0, len(diagnostic_report[0])):
    zero_count = 0;
    one_count = 0
    diagnostic_report = [x for x in diagnostic_report if x.startswith(co2)]
    if(len(diagnostic_report) == 1):
        co2 = diagnostic_report[0]
        break
    for measurement in diagnostic_report:
        if(measurement[i] == '0'):
            zero_count += 1
        else:
            one_count += 1
    print(i )
    print('0' + str(zero_count))
    print('1' + str(one_count))
    if zero_count > one_count:
        #oxygen += '0'
        co2 += '1'
    else:
        #oxygen += '1'
        co2 += '0'

print(int(oxygen,2) * int(co2, 2))
print(int(co2, 2))