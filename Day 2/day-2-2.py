inputfile = open("input.txt")
inputlist = []

for line in inputfile:
    line = line.split(" ")
    line[0] = list(map(int, line[0].split("-")))
    line[1] = line[1][0]
    line[2] = line[2].strip()
    inputlist.append(line)

count = 0

for i in inputlist:
    isvalid = False
    if (i[2][i[0][0] - 1] != i[1]) and (i[2][i[0][1] - 1] == i[1]) or (i[2][i[0][0] - 1] == i[1]) and (i[2][i[0][1] - 1] != i[1]):
        count = count + 1
        isvalid = True
        print(i[0][0],i[0][1], isvalid, i[1], i[2])

print(count)