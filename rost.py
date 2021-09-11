rost = []
with open('dataset_3380_5.txt') as inf:
    r = inf.readlines()
r1 = [line.strip().split() for line in r]
for i in range(len(r1)):
    rost[r1[i][0]].append(r1[i][2])

    print(r1[i][0], r1[i][2])
print(rost) 