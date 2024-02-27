ages = [12, 14, 34 , 25, 5]

names = ["baited", "onfire", "dxtr", "smoxx"]

print(names[0])
print(ages[0])

mylist = ["baited ", 20, 1.83, True]

print(mylist)

print(names[1])

ages[1] = 15

print(ages) 

ages.insert(1, 69)

print(ages)

ages.remove(12)

print(ages)

ages.append(12)

print(ages)

del ages[1]

print(ages)

lenth = len(names)

print(lenth)

minim = min(names)

print(minim)

maxim = max(names)

print(maxim)

for age in ages:
    print("age = ", age)

for x in range(len(ages)):
    print("age = ", ages[x])

THE_LIST = [["NAMES", "ARE"], ["WHAT", "WE"], ["USE", "NOW"]]

print(THE_LIST[1][0])