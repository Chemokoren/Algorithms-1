f = open("names.txt", "r")
maxname = "none"
maxval = 0
max2name = "none"
max2val = 0

for line in f:
    (name, sex, count) = line.rsplit(",")
    count = int(count)
    if sex == "F":
        if count > maxval:
            max2name = maxname
            max2val = maxval
            maxval = count
            maxname = name
        elif count > max2val:
            max2name = name
            max2val = count

print(maxname, max2name)
print(maxval, max2val)
