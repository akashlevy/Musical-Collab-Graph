# takes data in the format of top 10 lists and aggregates a rating
# 1. Trae Tha Truth: 0.26319335065 (60) degree: 269
# 2. Rick Ross: 0.233173296203 (82) degree: 81
# 3. Lil Wayne: 0.228159937465 (90) degree: 99
# 4. T.I.: 0.226115197565 (80) degree: 96
# 5. Ludacris: 0.201772441884 (77) degree: 100
# 6. Jeezy: 0.196197456087 (77) degree: 65


file = open("data.txt", "r")

def data(file):
	d = {}
	i = 0
	for line in file:
		if line.strip() != '':
			start = line.index(". ")
			key = line[start+2:line.index(":")]
			val = abs(i - 9) + 1
			i += 1
			i %= 10

			if key in d.keys():
				d[key] = d[key] + val
			else:
				d[key] = val

	for key in sorted(d.keys(), key=d.get, reverse=True):
		print key, d[key]

artists = data(file)
