def	get_winning_numbers(line):
	winning_n = []
	i = 10
	while line[i] != "|":
		number = -20
		while line[i].isdigit():
			number = number * 10 + int(line[i])
			i += 1
		if number != -20:
			winning_n.append(number)
		i += 1
	return winning_n

def	get_ticket_numbers(line):
	ticket_n = []
	i = 42
	while line[i] != '\n':
		number = -20
		while line[i].isdigit():
			number = number * 10 + int(line[i])
			i += 1
		if number != -20:
			ticket_n.append(number)
		if line[i] == '\n':
			break
		i += 1
	return ticket_n

def	check_points(winning_n, ticket_n):
	points = 0
	for n in ticket_n:
		if n in winning_n:
			if points == 0:
				points = 1
			else:
				points *= 2
	return points

def	main():
	f = open("/home/brumarti/Advent-Of-Code/adv_2023/day04/input.txt", "r")

	i = 1
	sum = 0
	line = f.readline()
	while line:
		winning_n = get_winning_numbers(line)
		ticket_n = get_ticket_numbers(line)
		points = check_points(winning_n, ticket_n)
		print("Game #" + str(i) + ": " + str(points) + " points")
		sum += points
		i += 1
		line = f.readline()
	print("Total points: " + str(sum))
	
if __name__ == "__main__":
	main()