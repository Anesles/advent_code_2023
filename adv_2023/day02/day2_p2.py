def	get_round(line, i):
	blue = 0
	red = 0
	green = 0

	while (line[i] != ';' and line[i] != '\n'):
		number = 0
		while line[i].isdigit():
			number = number * 10 + int(line[i])
			i += 1
		i += 1
		if line[i] == 'b':
			blue = number
		elif line[i] == 'r':
			red = number
		elif line[i] == 'g':
			green = number
		while line[i].isalpha():
			i += 1
		if line[i] == ',':
			i += 2
	return blue, red, green, i

def main():
	f = open("/home/brumarti/Advent-Of-Code/adv_2023/day02/input.txt", "r")

	sum = 0

	line = f.readline()
	while line:
		i = 8
		min_blue, min_red, min_green = 0, 0, 0
		while 1:
			blue, red, green, i= get_round(line, i)
			if blue > min_blue:
				min_blue = blue
			if red > min_red:
				min_red = red
			if green > min_green:
				min_green = green
			if line[i] == ';':
				i += 2
			elif line[i] == '\n':
				break
		power = min_blue * min_red * min_green
		sum += power
		line = f.readline()

	print("sum: ", sum)

if __name__ == "__main__":
	main()