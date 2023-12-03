def get_game_number(line):
	game_number = 0
	i = 5
	multiply = 0
	while line[i].isdigit():
		game_number = game_number * 10 + int(line[i])
		i += 1
		multiply += 1
	return game_number

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

def verify_round(blue, red, green):
	if red > 12 or blue > 14 or green > 13:
		return 1
	return 0

def main():
	f = open("/home/brumarti/Advent-Of-Code/adv_2023/day02/input.txt", "r")

	sum = 0

	line = f.readline()
	while line:
		game_number = get_game_number(line)
		i = 4
		while line[i] != ':':
			i += 1
		i += 2
		state = 0
		while 1:
			blue, red, green, i= get_round(line, i)
			if state == 0:
				state = verify_round(blue, red, green)
			if line[i] == ';':
				i += 2
			elif line[i] == '\n':
				break
		if state == 0:
			sum += game_number
		line = f.readline()
	print("sum: ", sum)

if __name__ == "__main__":
	main()
