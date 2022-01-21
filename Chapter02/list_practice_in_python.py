"""
for i in range(10):
    print('iteration => ' + str(i))
"""

list1 = [22, 11, 15, 7, 2, 0, 88]

# get the type
print(list1.__class__)

print(list1.pop(0), 'popped')  # pop mutate the original list (pop returns value popped)
list1.append(11)  # append mutate the original list
list1.insert(0, 222)  # insert mutate the original list
print(list1.index(11), ' => index of 11')  # gets the first index of this value
list1.sort()
print(list1, "sorted")
list1.reverse()
print(list1, "reversed")

print("Counting a value 11 => ", list1.count(11))

print('--------------------------')

# loop starts from index 1
for i in range(1, len(list1)):
    print(list1[i])

print('--------------------------')
list1.clear()

print(list1)
