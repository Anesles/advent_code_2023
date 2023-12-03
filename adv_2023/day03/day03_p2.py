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
			j += 1
	i += 1

if __name__ == "__main__":
	main()