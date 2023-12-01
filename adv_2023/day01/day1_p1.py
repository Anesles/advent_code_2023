f = open("/home/brumarti/Advent-Of-Code/adv_2023/day01/input.txt", "r")

sum = 0
last = 0
first = -20
number = 0

line = f.readline()
while line:
	for c in line:
		if c.isdigit():
			if first == -20:
				first = int(c)
			last = int(c)
	number = (first * 10) + last
	sum += number
	first = -20
	last = 0
	line = f.readline()
print("sum: ", sum)