import random
from tabulate import tabulate
from collections import OrderedDict

filename = "languages"
with open(filename, "r") as f:
	lang = f.readlines()
	lang = map(str.strip, lang)

score = [0] * len(lang)
final_dict = {}
final_list = []

i = 0
COUNT = len(lang) * 1000
while i < COUNT:
	ctr = random.choice(lang) 
	score[lang.index(ctr)] += 1
	i += 1

sum_score =  sum(score)

ctr = 0
for i in score:
	final_dict[lang[ctr]] = (float(i) / sum_score) * 100
	ctr += 1


od = OrderedDict(sorted(final_dict.items(), key=lambda(k,v):(v,k), reverse=True))

for i in od:
	final_list.append([i, od[i]]);

print_headers = ["Language", "Percentage Score"]
print tabulate(final_list, headers= print_headers, tablefmt='orgtbl')
