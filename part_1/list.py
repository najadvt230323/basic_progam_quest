thislist=list(("apple","banana","cherry","orang","kiwi"))
print(thislist[-3:-1])
if "apple" in thislist:
    print("yes,apple is in tha fruits list")
else:
    print("no,apple is'nt in tha fruits list")
# thislist[1]="blakcurrant"
# print(thislist)
# thislist[1:3]=["apple","kiwi"]
# print(thislist)


# thislist.insert(2,"mango")
# print(thislist)

newlist=["jackfruit","mango"]
# thislist.insert(2,newlist)
print(thislist)

# thislist.extend(newlist)
print(thislist)

newlist.extend(thislist)
print(newlist)

newlist.remove("apple")
print(newlist)
print(len(newlist))

newlist.pop(1)
print(newlist)

del newlist[0]
print(newlist)
print(type(newlist))


sentence = ' '.join(newlist)
print(sentence)
print(type(sentence))
print(sentence[:3])
print(sentence[:-3])
print(sentence[-3:])
print(sentence[::-1])
print(sentence[::-2])
print(sentence[::-3])




newlist.clear()
print(newlist)

