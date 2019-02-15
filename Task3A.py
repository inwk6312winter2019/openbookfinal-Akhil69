import string
fp1=open('Book1.txt') #opening and reading the books
file1=fp1.read()
fp2=open('Book2.txt')
file2=fp2.read()
fp3=open('Book3.txt')
file3=fp3.read()
def sorted_words(book):
	count=0
	mydict=dict()
	book_list=[]
	for line in book.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		book_list.append(myword)
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1
	sort_list=[]

	for char in mydict:   # we get the words in sortingorder
		sort_list.append(char)
	sort_list.sort(reverse=True)
	print(sort_list)



print("",sorted_words(file1)) 
print("",sorted_words(file2)) 
print("",sorted_words(file3)) 

