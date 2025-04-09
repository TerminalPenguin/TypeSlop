# ptr <string> (print)
# ptr* var (Should prob be setup after variables)
# setting variables: "set <type> <name> <value>"
# types: string, int, float
variables = {'mystring':'hi'}
with open('main.txt') as f:
	lines = f.readlines()
	for line in lines:
		if line.startswith('prt'):
			prtsplit = line.split(' ')
			del prtsplit[0]
			prtvalue = ' '.join(prtsplit)
			print(prtvalue)
		if line.startswith('prt*'):
			prtsplit = line.split(' ')
			print(len(prtsplit))
			del prtsplit[0]
		if line.startswith('set'):
			setsplit = line.split(' ')
			varType = setsplit[1]
			varName = setsplit[2]
			if varType == 'string':
				del setsplit[0:3]
				print(setsplit)
				lastsplit = [char for char in setsplit[-1]]
				print(lastsplit)
				del lastsplit[-1]
				del setsplit[-1]
				setsplit.append(''.join(lastsplit))
				print(setsplit)
				stringValue = ' '.join(setsplit)
				variables[varName] = stringValue
