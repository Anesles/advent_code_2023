def transform(number):
	if number == 'one':
		return 1
	elif number == 'two':
		return 2
	elif number == 'three':
		return 3
	elif number == 'four':
		return 4
	elif number == 'five':
		return 5
	elif number == 'six':
		return 6
	elif number == 'seven':
		return 7
	elif number == 'eight':
		return 8
	elif number == 'nine':
		return 9

def	find_number(line, i):
	number = ''
	digits_t = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

	while i < len(line):
		c = line[i]
		if c.isdigit():
			break
		else:
			number += c
			for n in digits_t:
				if n in number:
					return transform(n), i
		i += 1
	return None, i
	

f = open("/home/brumarti/Advent-Of-Code/adv_2023/day01/input.txt", "r")

sum = 0
last = 0
first = -20

line = f.readline()
while line:
	for i in range(len(line)):
		c = line[i]
		if c.isdigit():
			if first == -20:
				first = int(c)
			last = int(c)
		else:
			number, i= find_number(line, i)
			if number != None:
				if first == -20:
					first = int(number)
				last = int(number)
		i += 1
	sum += (first * 10) + last
	print("sum: ", sum, "number: ", (first * 10) + last)
	first = -20
	line = f.readline()