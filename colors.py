colors = [
	"1f77b4",
	"aec7e8",
	"ff7f0e",
	"ffbb78",
	"2ca02c",
	"98df8a",
	"d62728",
	"ff9896",
	"9467bd",
	"c5b0d5",
	"8c564b",
	"c49c94",
	"e377c2",
	"f7b6d2",
	"7f7f7f",
	"c7c7c7",
	"bcbd22",
	"dbdb8d",
	"17becf",
	"9edae5",
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