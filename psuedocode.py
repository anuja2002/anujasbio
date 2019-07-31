ages = [5, 12, 3, 56, 24, 78, 1, 15 ,44]
ages.sort()
total = 0
for age in ages:
    total = total + age
average = total/len(ages)
print(average)
