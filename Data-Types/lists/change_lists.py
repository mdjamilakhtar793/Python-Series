thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)