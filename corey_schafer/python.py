# '' vs ""
message = "Hello world"

print(message.count('b')) #returns the number of occurences in the string
print(message.find('world')) #returns the first index of the occurence

# print(message.replace('world', 'universe')) #replaces the first occurence of the string with the new string

new_message = message.replace('world', 'universe')
print(new_message) #replaces the first occurence of the string with the new string

greeting = 'Hello'
name = 'Karthik'

message = greeting + ', ' + name + '. Welcome!'
print(message) #concatenates the two strings
message = '{}, {}.Welcome!'.format(greeting,name) # string formatting
print(message)

#f-strings 
message = f'{greeting}, {name.lower()}. Welcome!' # string formatting using f-strings
print(message)

# print(dir(name)) #dir returns the list of attributes and methods for the object
# print(help(str)) #help returns the documentation for the object

