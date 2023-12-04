COPIES = 1
MATCHING = 0

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

def	check_matching(winning_n, ticket_n):
	matching_n = 0
	for n in ticket_n:
		if n in winning_n:
			matching_n += 1
	return matching_n

def	iterate_scratch(scratch):
	i = 0

	size = 0
	while i < len(scratch):
		size += scratch[i][COPIES]
		matching = scratch[i][MATCHING]
		j = i + 1
		while j <= (matching + i):
			tu = list(scratch[j])
			tu[COPIES] += scratch[i][COPIES]
			scratch[j] = tuple(tu)
			j += 1
		i += 1
	return size


def	main():
	f = open("/home/brumarti/Advent-Of-Code/adv_2023/day04/input.txt", "r")

	i = 0
	scratch = []
	line = f.readline()
	while line:
		winning_n = get_winning_numbers(line)
		ticket_n = get_ticket_numbers(line)
		matching_n = check_matching(winning_n, ticket_n)
		scratch.append((matching_n, 1))
		i += 1
		line = f.readline()
	size = iterate_scratch(scratch)
	print(size)

if __name__ == "__main__":
	main()