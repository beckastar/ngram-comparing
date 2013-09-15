# -*- coding: utf-8 -*-
import regex as re
import unicodedata 
import string

#open file, convert text to string 
f = open ("fearandloathing.txt", "r") 
s = f.read().replace('\n', '')

def remove_punctuation(s):
    s =  re.sub(ur"\p{P}+", "", s)
    print "working"
    return s


s = remove_punctuation(s)
s = s.lower()
for word in s:
	try:
		word.encode("ascii", "ignore")
	except UnicodeDecodeError:
		pass

print s 

def bigrams(s):
	bigrams = {}
	for word in range(len(s)-3):
		key = (s[word], s[word+1])
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
# 		print "more than one", gram, ngrams[gram]
 



# print ngrams

# def find_trigrams():


# def find_quadgrams():


# def find_quintgrams():

# def find_sextograms():





# def find_bigrams():
# 	return zip(s, s[1:])
