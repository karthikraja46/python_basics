#in this file we are going to learn about list tuple and dictionaries
#tuples will work with the sequential data
#lists will work with the non sequential data
#sets are unordered collection of unique elements
#dictionaries are unordered collection of key value pairs
#lists are mutable
#tuples are immutable
#sets are mutable
#dictionaries are mutable

courses = ['history', 'math', 'physics', 'computers']
print(len(courses)) #returns the length of the list
print(courses[0:2]) #returns the first element of the list
print(courses[0]) #returns the first element of the list
print(courses[1:3]) #returns the elements from index 1 to 3
print(courses[1:]) #returns the elements from index 1 to the end of the list
print(courses[:3]) #returns the elements from the beginning of the list to index 3
print(courses[-1]) #returns the last element of the list
print(courses[-2:]) #returns the last two elements of the list
print(courses[3])

#Modifying the list
courses.append('art') #adds the element to the end of the list
courses.insert(0, 'art') #adds the element to the beginning of the list
print(courses.count('art'))
print(courses.index('art')) #returns the index of the element
print(courses.extend('math')) #adds the element to the end of the list
print(courses.pop())

string = 'mom'
is_palindrome = True
if string == string[::-1]:

    is_palindrome = True
    is_palindrome = False
print(is_palindrome)
#list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
courses = ['history', 'math', 'physics', 'computers']
#looping through the list
# for i in courses:
#     print(i)
# using enumerate function to get the index and value
# for index, course in enumerate(courses):
#     print(index, course)
# for index, course in enumerate(courses, start=1):
#     print(index, course)

# courses = ['history', 'math', 'physics', 'computers']


# courses_str = ', '.join(courses) #joins the list into a string

# new_list = courses_str.split(' - ') #splits the string into a list
# print(new_list)

# tuples are immutable 

tuples1 = ('history', 'math', 'physics', 'computers')
tuple2 = tuples1
print(tuples1)
print(tuple2)

# tuples1[0] = 'art' # this will raise an error because tuples are immutable
#sets
cs_courses = {'history', 'math', 'physics', 'computers'}
ar_courses = {'history', 'math', 'physics', 'computers'}
print(cs_courses.intersection(ar_courses)) #returns the intersection of the two sets
print(cs_courses.difference(ar_courses)) #returns the difference of the two sets




