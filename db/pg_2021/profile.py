import json

with open('profiles.json') as f:
	data = json.load(f)

for i in range(len(data)):
	with open(data[i]['roll']+'.json', 'w') as f:
		json.dump(data[i], f)