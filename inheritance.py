# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# class Dog:
    
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
    
#     def bark(self):
#         print('bowwww........')

# my_dog = Dog("Buddy", "Golden Retriever")
# my_dog.bark()


# class Mobile:
    
#     def __init__(self, brand, battery, ram, camera, price):
#         self.brand = brand
#         self.battery = battery
#         self.ram = ram
#         self.camera = camera
#         self.price = price
    
#     def display(self):
#         print("Brand:", self.brand)
#         print("Battery:", self.battery)
#         print("Ram:", self.ram)
#         print("Camera:", self.camera)
#         print("Price:", self.price)

# obj = Mobile("apple", '4000mah', '8gb', '48mp', '90000')
# obj.display()#Calling a method

# single inheritance
# class Parent:
#     def fun1(self):
#         print('this is parent class')

# class Child(Parent):
#     def fun2(self):
#         print('this is child class')

# obj = Child()
# obj.fun2()
# obj.fun1()


# # Multi level Inheritance
# class Parent:
#     def fun1(self):
#         print('this is parent class')

# class Child(Parent):
#     def fun2(self):
#         print('this is child class')
        
# class GrandChild(Child):
#     def fun3(self):
#         print('this is child class')
        
# obj = GrandChild()
# obj.fun1()
# obj.fun2()
# obj.fun3()

#Hierarichal Inheritance

# class Parent:
#     def fun1(self):
#         print('this is parent class')

# class Child1(Parent):
#     def fun2(self):
#         print('this is child class')
        
# class Child2(Parent):
#     def fun3(self):
#         print('this is grandchild class')
        
# obj = Child2()
# obj.fun1()
# # obj.fun2()
# obj.fun3()

#super keyword

# class A:
    
#     def __init__(self):
#         print('this is class A')
    
#     def fun1(self):
#         print('this is father class')

# class B(A):
#     def __init__(self):
#         print('this is class B')
#         super().__init__()

#     def fun2(self):
#         print('this is mother class')
# obj = B()
# obj.fun2()


# Polymorphism

# Complile time polymorphism
#method overloading
#same class 
#same function names or method names
#different parameters

# class A:
#     def sum(self, a, b):
#         print('sum:', a+b)
    
#     def sum(self, a, b, c):
#         print('sum:', a+b+c)

# obj = A()
# print(obj.sum(1,2,5))


# #run time polymorphism
# #method overriding
# #different parameters
# #same function names or method names

# class A:
#     def display(self):
#         print('this is class A')
# class B(A):
#     def display(self):
#         print('this is class B')
#         super().display()

# obj = B()
# obj.display()


#Abstraction 
#abstract class(hiding of data)

