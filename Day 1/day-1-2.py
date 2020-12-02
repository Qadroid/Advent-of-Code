
inputfile = open("input.txt")
inputlist = []

for line in inputfile:
    line = line.strip()
    inputlist.append(line)

inputlist = list(map(int, inputlist))

print(inputlist)

for i in inputlist:
    for i2 in inputlist:
        for i3 in inputlist:
            if i + i2 + i3 == 2020:
                print("First number is equal to: ", i)
                print("Second number is equal to: ", i2)
                print("Third number is equal to: ", i3)
                print("Product of both numbers is equal to: ", i * i2 * i3)

inputfile.close()