with open("owoce.txt", "r", encoding="utf-8") as f:
    lines = f.read().strip().splitlines()

date = []
raspberries = []
strawberries = []
currant = []

for line in lines[1:]:
    section = line.split()
    date.append(section[0])
    raspberries.append(section[1])
    strawberries.append(section[2])
    currant.append(section[3])

print(raspberries)

counter = 0
for i in range(len(currant)):
    if int(currant[i]) > int(strawberries[i]) and int(currant[i]) > int(raspberries[i]):
        counter += 1

print(counter)

#Ex6.3
rasp_straw = 0
rasp_currant = 0
straw_currant = 0