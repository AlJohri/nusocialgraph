# https://github.com/mbostock/d3/wiki/Ordinal-Scales

colors = [
	'1f77b4',
	'ff7f0e',
	'2ca02c',
	'd62728',
	'9467bd',
	'8c564b',
	'e377c2',
	'7f7f7f',
	'bcbd22',
	'17becf',
	'aec7e8',
	'ffbb78',
	'98df8a',
	'ff9896',
	'c5b0d5',
	'c49c94',
	'f7b6d2',
	'c7c7c7',
	'dbdb8d',
	'9edae5',
]

def hex_to_rgb():
	cList = []
	for hex_digits in colors:
		rgbDict = {}
		rgb = tuple([int(s, 16) for s in (hex_digits[0:2], hex_digits[2:4], hex_digits[4:6])])
		rgbDict['r'] = rgb[0]
		rgbDict['g'] = rgb[1]
		rgbDict['b'] = rgb[2]
		cList.append(rgbDict)
	return cList

rgbs = hex_to_rgb()