def unique_words(book):
    mylist = []
    f = open(book1,"r")
    for re in f:
        re = re.strip()
        re = re.split()
        for r in re:
            if r != "": 
                if r not in mylist:
              #  re = re.strip()
                    mylist.append(r)
    mytuple = tuple(mylist)
    return mytuple

var = input("enter name of book:")
print("Output is:",unique_words(var))


