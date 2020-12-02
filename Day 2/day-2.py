inputfile = open("input.txt")
inputlist = []

for line in inputfile:
    line = line.split(" ")
    line[0] = line[0].split("-")
    line[1] = line[1][0]
    line[2] = line[2].strip()
    inputlist.append(line)

count = 0

for i in inputlist:
    if i[2].count(i[1]) in range(int(i[0][0]), int(i[0][1]) + 1):
        count = count + 1

print(count)