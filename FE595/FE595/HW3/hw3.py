from flask import Flask
import requests

# This part I tried two ways, one for split sentence by '.', another way to find "she's" and "they"
# Due to there are some sentence Do NOT have '.' between He and She, so I decide use second method.

male = list()
female = list()
for i in range(50):
	r = requests.get('https://theyfightcrime.org/')
	rest = r.text.split('<P>')
	M = rest[1].find(" She's")
	F = rest[1].find(" They fight")
	#male.append(rest[1].split('.')[0] +"\n")
	#female.append(rest[1].split('.')[1] +"\n")
	male.append(rest[1][:M] +"\n")
	female.append(rest[1][M+1:F]+"\n")

with open('male.txt', 'w') as m:
	m.writelines(male)

with open('female.txt', 'w') as f:
	f.writelines(female)

print ('Finished')
