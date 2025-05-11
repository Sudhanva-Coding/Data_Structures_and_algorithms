x1 = [2, 90, 34, 5, 1]
#x2 = x1.sort()
x1.sort(reverse= False)

print("ascending order output : ", x1)

x1.sort(reverse = True)
print("descending order output : ", x1.sort(reverse= True))
print("\n")

# bubble sort
mylist = [12, 34, 2, 5, 7]
#print("count of items are : ", len(mylist))
for i in range(0, len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i], mylist[j] = mylist[j], mylist[i]
print("The output of bubble sort in descending order is : ", mylist)

# selection sort
mylist = [12, 34, 2, 5, 7]
for i in range(0, len(mylist)):
    min_element = 10000000
    min_location = -1
    for j in range(i, len(mylist)):
        if min_element > mylist[j]:
            min_element = mylist[j]
            min_location = j
            mylist[i], mylist[j] = mylist[j], mylist[i]

print("the output of selection sort is : ", mylist)

