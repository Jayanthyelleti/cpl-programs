# Jayanth Adithya Yelleti
#jay26@njit.edu
def safe(Q, r, c):

#column
	for i in range(r):
		if Q[i][c] == 'Q':
			return False
#diagonal
	(i, j) = (r, c)
	while i >= 0 and j >= 0:
		if Q[i][j] == 'Q':
			return False
		i = i - 1
		j = j - 1
	(i, j) = (r, c)
	while i >= 0 and j < len(Q):
		if Q[i][j] == 'Q':
			return False
		i = i - 1
		j = j + 1

	return True


def print_board(Q):
	for r in Q:
		print(str(r).replace(',', '').replace('\'', ''))
	print()


def find_solutions(Q, r):
	if r == len(Q):
		print_board(Q)
		return
	for i in range(len(Q)):
		if safe(Q, r, i):
			Q[r][i] = 'Q'

			find_solutions(Q, r + 1)
			Q[r][i] = '–'
if __name__ == '__main__':
	N = 8
	Q = [['–' for x in range(N)] for y in range(N)]
	find_solutions(Q, 0)
