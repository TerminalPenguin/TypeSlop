exe = 'main.txt'

with open(exe, 'r') as f:
	lines = [line.rstrip('\n') for line in f]
print(lines_without_newline)
