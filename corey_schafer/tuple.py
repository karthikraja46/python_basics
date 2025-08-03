#tuple is a collection of the objects seperate dby commas
# we can declare them using a bracket
#unlike list is immutable
#we cannot add delete append or extend any element once it is created
#Tuple cannot be declared with single elemnt if so then add
#slice is get a portion from the list or tuple

tup1 = ("DSA","leetcode")
print(tup1)
print(type(tup1))
print(tup1[0])

tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3)
print(tup3[1:4])
print(tup3[1:5])


dict = {}
print(dict)
print(type(dict))


dict1 = {"name":"sivam","age":23,"city":"delhi"}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

for key,values in dict1.items():
    print(key,values)