with open("pi_przyklad.txt", "r", encoding="utf-8") as f:
    lines = f.read().strip().splitlines()
#Ex3.1
double = []
count = 0
for i in range(len(lines) - 1):
    first = int(lines[i])
    second = int(lines[i + 1])
    fragment = first * 10 + second
    double.append(fragment)
for j in range(len(double) - 1):
    if double[j] > 90:
        count = count + 1
#Ex3.2
doubles =[0 for i in range(100)]
k = 0
j=0
while k < 100:
    for i in range(len(double)):
        if k == double[i]:
            doubles[j] += 1
    k = k + 1
    if j < len(doubles)-1:
        j = j + 1

print(doubles)
print(doubles[62])
#Ex3.3
sixths = []
pos = []

for i in range(len(lines) - 5):
    first  = int(lines[i])
    second = int(lines[i + 1])
    third  = int(lines[i + 2])
    fourth = int(lines[i + 3])
    fifth  = int(lines[i + 4])
    sixth  = int(lines[i + 5])

    if first <= second <= third >= fourth >= fifth >= sixth:
        sixths.append(first*100000 + second*10000 + third*1000 + fourth*100 + fifth*10 + sixth)
        pos.append(i)

print(sixths)
print(pos)
#Ex3.4
maxi = sixths[0]
for i in range(len(sixths)):
    if sixths[i] > maxi:
        maxi = i
print("Largest consecutive one is at " + sixths[maxi] + ", " + pos[maxi])
