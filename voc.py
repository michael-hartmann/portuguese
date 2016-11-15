from sys import argv
from random import shuffle

def slurp(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue
            left, right = line.split(";")
            data.append((left.strip(), right.strip()))
    return data


filename = argv[1]
data = slurp(filename)

shuffle(data)

f = open("erro.csv", "a")

total = len(data)
correct = 0
for i,(left,right) in enumerate(data):
    entry = input("[%d/%d] " % (i+1,total) + left + ": ")
    entry = entry.strip()
    if entry != right:
        print("Falsch: Eingabe \"%s\", korrekt \"%s\"" % (entry, right))
        print("%s; %s" % (left,right), file=f)
    else:
        correct += 1

f.close()
print("%d/%d (%.2f%%)" % (correct, total, correct/total*100))
