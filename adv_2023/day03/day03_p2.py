def check_gear(engine, i, index, lines):
	c_num = 0
	if i > 0:
		c = engine[i - 1][index]
		if c == '.':
			if engine[i - 1][index - 1].isdigit():
				c_num += 1
			if engine[i - 1][index + 1].isdigit():
				c_num += 1
		else:
			if c.isdigit():
				c_num += 1
	if i < lines - 1:
		c = engine[i + 1][index]
		if c == '.':
			if engine[i + 1][index - 1].isdigit():
				c_num += 1
			if engine[i + 1][index + 1].isdigit():
				c_num += 1
		else:
			if c.isdigit():
				c_num += 1
	if engine[i][index - 1].isdigit():
		c_num += 1
	if engine[i][index + 1].isdigit():
		c_num += 1
	if c_num == 2:
		return 1
	return 0

def write_number(map, i, j):
	index = j

	number = 0
	end = j
	while map[i][j].isdigit():
		end = j
		j += 1
	j = index
	start = j
	while map[i][j].isdigit():
		start = j
		j -= 1
	number = 0
	while start <= end:
		number = number * 10 + int(map[i][start])
		start += 1
	return number

def get_numbers(map, i, j, lines):
	number1 = 0
	number2 = 0

	found = 0
	start = j - 1
	end = j + 1
	if i > 0:
		while start <= end:
			while map[i - 1][start].isdigit() and start <= end:
				found = 1
				start += 1
			if found == 1:
				if number1 == 0:
					number1 = write_number(map, i - 1, start - 1)
				else:
					number2 = write_number(map, i - 1, start - 1)
				found = 0
			else:
				start += 1
	start = j - 1
	end = j + 1
	if i < lines - 1:
		while start <= end:
			while map[i + 1][start].isdigit() and start <= end:
				found = 1
				start += 1
			if found == 1:
				if number1 == 0:
					number1 = write_number(map, i + 1, start - 1)
				else:
					number2 = write_number(map, i + 1, start - 1)
				found = 0
			else:
				start += 1
	if map[i][j - 1].isdigit():
		if number1 == 0:
			number1 = write_number(map, i, j - 1)
		else:
			number2 = write_number(map, i, j - 1)
	if map[i][j + 1].isdigit():
		if number1 == 0:
			number1 = write_number(map, i, j + 1)
		else:
			number2 = write_number(map, i, j + 1)
	return number1, number2
				
def main():
	f = open("/home/brumarti/Advent-Of-Code/adv_2023/day03/input.txt", "r")

	sum = 0
	engine = f.readlines()
	lines = len(engine)
	cols = len(engine[0]) - 1

	i = 0
	while i < lines:
		j = 0
		while j < cols:
			if engine[i][j] == '*':
				if check_gear(engine, i, j, lines):
					number1, number2 = get_numbers(engine, i, j, lines)
					print("Found valid gear at line", i, "and column", j, "with numbers", number1, "and", number2)
					sum += number1 * number2
			j += 1
		i += 1
	print("Sum:", sum)

if __name__ == "__main__":
	main()