# -*- coding: utf-8 -*-
import regex as re
import unicodedata 
import string
import nltk

#open file, convert text to string 
f = open ("fearandloathing.txt", "r") 
s = f.read().replace('\n', '')

def remove_punctuation(s):
    s =  re.sub(ur"\p{P}+", "", s)
    return s

s = remove_punctuation(s)
s = s.lower()
for word in s:
	try:
		word.encode("ascii", "ignore")
	except UnicodeDecodeError:
		pass


def ngrams(s):
	s = s.split()
	l = []
	n = range(6)
	for word in range(len(s)-n+1):
		key = (s[word:word+n])
		l.append(key)
		print l
	return l

print ngrams

# def count_ngrams(ngrams):
# 	ngrams = {}


def bigrams(s):
	bigrams = {}
	trigrams = {}
	for n in range(4):
		for word in range(len(s)-(n-1)):
			key = range(s[word], s[word+n])
			l = bigrams.get(key)
			if l == None:
				bigrams[key] = 1
			else:
				bigrams[key] += 1
		return bigrams



# n = range(10)
# ngrams = {}
# i = 2
# for word in range(len(s)-3): 
# 		gram = (s[word],s[word+1],s[word+2])
# 		l = ngrams.get(gram)
# 		if l != None:
# 			ngrams[gram]+=1
# 		else:
# 			ngrams[gram]=1


# for gram in ngrams:
# 	if ngrams[gram] > 1:
# 		print "more than one", gram, ngrams[gra