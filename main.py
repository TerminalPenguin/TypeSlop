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
		if line.startswith('set'):
			setsplit = line.split(' ')
			print(setsplit[2])
			varType = setsplit[1]
			varName = setsplit[2]
			if varType == 'string':
				del setsplit[0:3]
				stringValue = ' '.join(setsplit)
				print(stringValue)
				variables[varName] = stringValue
				print(variables)
			else:
				print(f"error occured:'  {line}  ' set variable type {varType} is not valid type")
