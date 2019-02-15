import re #importing regex
from collections import Counter
#here we importing Counter module to track how many equivalent words are there
def test_bk1():
	with open('Book1.txt') as f: #openning the file
	    text = f.read().lower()
	words = re.findall(r'\w+', text) #Here we are using regex 
	print(Counter(words).most_common(20))
test_bk1()
def test_bk2():
	with open('Book2.txt') as f: 
	    text = f.read().lower()
	words = re.findall(r'\w+', text)
	print(Counter(words).most_common(20))
test_bk2()
def test_bk3():
	with open('Book3.txt') as f:
	    text = f.read().lower()
	words = re.findall(r'\w+', text)
	print(Counter(words).most_common(20))
test_bk3()
