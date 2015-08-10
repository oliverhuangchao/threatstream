# anagram Mapreduce edition

# we can use print edition
# or we can juse list edition
import sys


check = {'aaa':'dream','bbb':'the'}

def run(word):
	if word[:2] == "<%" and word[-2:] == "%>" and word[2:-2] in check:
		word = check[word[2:-2]]
	return word

current_word = None
current_count = 0
res = list()
for line in sys.stdin:
	line = line.strip()
	words = map(run,line.split(' '))
	line = ' '.join(words)
	print line
	
#print res