# Written by Darksky

from os import system

hex_mapping = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, '0':0}
rhex_mapping = {}
for item in hex_mapping.items():
	rhex_mapping[item[1]] = item[0]
color_mapping = {(0,0,0):'Black Dye', (1,0,0):'Red Dye', (0,1,0):'Lime Dye', (0,0,1):'Blue Dye', (1,1,1):'White Dye', (1,1,0):'Yellow Dye', (0,1,1):'Cyan Dye', (1,0,1):'Magenta Dye'}
agree_list = ['y', 'Y', 'yes', 'YES', 'Yes']

def hexColorTuple(color):
	hexc = '#'
	for val in color:
		fpos = val // 16
		spos = val % 16
		hexc += rhex_mapping[fpos] + rhex_mapping[spos]
	return hexc

def getColorTuple(colors: str):
	cooked = ''
	for char in colors:
		if char.isalpha():
			cooked += char.lower()
		else: cooked += char
	colors = cooked		
	result = []
	inqueue = [colors[index:index+2] for index in range(0, 5, 2)]
	for chex in inqueue:
		val = hex_mapping[chex[0]] * 16
		val += hex_mapping[chex[1]]
		result.append(val)
	return tuple(result)

def upperDiv(n):
	return (n+1)//2 if n%2 else n // 2

def makeRGB(first_make: tuple):
	result = [0,0,0]
	for inx in range(3):
		if first_make[inx] == 1:
			result[inx] = 255
	return result

if __name__ == '__main__':
	while True:
		print('Insert #HEX code of a color or RGB values seperated by space.')
		raw_input = input('Your input:')

		if raw_input[0] == '#': targettp = getColorTuple(raw_input[1:])
		else: targettp = tuple(map(int, raw_input.split()))
		print('Target color(RGB):', targettp)

		pstr_list = []
		for target in targettp:
			process_str = bin(target<<1)[2:]
			process_str = '0' * (9-len(process_str)) + process_str
			process_str = process_str[::-1]
			pstr_list.append(process_str)

		adder = [[255, 255, 255], [255, 255, 254]]
		make_list = []
		for rep in range(9):
			make_list.append(tuple([int(pstr_list[index][rep]) for index in range(3)]))
			
		saved = make_list.pop(0)
		rgb = makeRGB(saved)
		for step in make_list:
			for index in range(3):
				if step[index] == 1:
					rgb[index] += adder[1 if step == (1,0,1) else 0][index]
				rgb[index] = upperDiv(rgb[index])
		print('Nearest color with Binary Blend:\n',rgb)
		print('\nOne possible blending method:')

		rgb = makeRGB(saved)
		material_map = {}
		material_map[saved] = 1
		print(f'Start with {color_mapping[saved]} ->', hexColorTuple(rgb), rgb)
		for step in make_list:
			if material_map.get(step, None) == None:
				material_map[step] = 1
			else: material_map[step] += 1
			for index in range(3):
				if step[index] == 1:
					rgb[index] += adder[1 if step == (1,0,1) else 0][index]
				rgb[index] = upperDiv(rgb[index])
			print('Blend with',color_mapping[step],'->',hexColorTuple(rgb), rgb)

		print('\nPossible needed materials:')
		for item in material_map.items():
			print('{:<15} x'.format(color_mapping[item[0]]), item[1])
		
		ifconti = input('\nContinue to blend other color?[y/N]:')
		if ifconti not in agree_list: break
		else: system('cls')
