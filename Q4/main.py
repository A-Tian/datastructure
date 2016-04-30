from UnorderedListModule import UnorderedList

ulist = UnorderedList()
ulist.add(10)
print(ulist.isEmpty())
ulist.remove(10)
print(ulist.isEmpty())
ulist.add(35)
ulist.add(20)
ulist.append(59)
print(ulist.index(35))
print(ulist.index(59))