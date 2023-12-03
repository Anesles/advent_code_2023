def check_line(line, start, end):
	i = start - 1
	if i < 0:
		i = 0
	while i <= end + 1:
		if line[i] != '.' and not line[i].isdigit() and line[i] != '\n':
			return 1
		i += 1
	return 0

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
			while (not engine[i][j].isdigit()) and engine[i][j] != '\n':
				j += 1
			if engine[i][j] == '\n':
				break
			start = j
			number = 0
			while engine[i][j].isdigit():
				number = number * 10 + int(engine[i][j])
				j += 1
			end = j - 1
			state = 0
			if i > 0:
				state = check_line(engine[i - 1], start, end)
			if (state == 0) and (i < lines - 1):
				state = check_line(engine[i + 1], start, end)
			if start == 0:
				if (state == 0) and engine[i][end + 1] != '.' and engine[i][end + 1] != '\n':
					state = 1
			else:
				if (state == 0) and (engine[i][start - 1] != '.' or engine[i][end + 1] != '.') and engine[i][end + 1] != '\n':
					state = 1
			if state == 1:
				print("Added number", number, "from line", i)
				sum += number
		i += 1
	print(sum)

if __name__ == "__main__":
	main()
