# Requires https://pypi.python.org/pypi/toposort
# Install with pip install toposort

from toposort import toposort, toposort_flatten
import csv

questbook = {}

with open('dag.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		questbook[int(row[0])] = set(int(x.strip()) for x in row[1].split(',') if x.strip().isdigit())

questmap = {}

for i, questset in enumerate(list(toposort(questbook))):
	print "!!!!", i
	for quest in sorted(questset):
		questmap[quest] = i
		print quest, questmap[quest]
		print ''

print '------------------'
for key in sorted(questmap.keys()):
	print questmap[key]
