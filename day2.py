# Built in functions

#print(len("hello world.  ")) # len counts the number of characters including the spaces
#print(float(12)) # -> 12.0
#x = input('what is your name: ')
#print('hello: ' + x)


import math


first_name = "john"
last_name = "smith"
country = "finland"
age = 33
married = True

person_info = {
    'firstname' : 'ronald',
    'lastname' : 'mcdonald',
    'age' : 23,
    'married':False,
    'country': 'mexico',

}

# person_info_second = {
#     firstname = 'ronald',
#     lastname = 'mcdonald',
#     age = 23,
#     married =False,
#     country = 'mexico'
# }


#what is a class? 
'''
    a class is a blueprint for creating objects.
  
    The class defines the shape, and each object like a person, car, or animal (like p1 = Person(...)) is a cookie made from that mold.
   
    it defines what attributes(data) and what behaviors(methods) the object will have, person is name, age ..., car is make model, color, animal is feet number, eyes count, tail
   
    classes must be named similar to naming a function so in our case class Person : 
            Why there’s a colon : after the class name : Why there’s a colon : after the class name, its also used in if statements
   
'''

    #def is short for 'defining a function' 

   # __init__ 
'''
        is a constructor and assigns the instance created aka person1 values like name, age or animal values like feet or eyes to the class. 
         
         in javascript it would be class Person{constructor(firstname,lastname,age)this.firstname=firstname;this.lastname=lastname} but in python it works the same just using --init-- instead of constructor
       
        the difference from javascript is there must be a 'self' in the constructor () where JS would use 'this' python uses self and it must be the first parameter
           
             why?: when you call the instance person1 = Person("John", "Smith") python doesn't just move it it translates it to the class Person.__init__(person1 = Person("John", "Smith")
           
                if you skip the self python won't know what is being assigned as the variables you create only live within that specific class and method
'''

    # By default, when you print an object, you get something like: <__main__.Person object at 0x104f2ffd0>
'''
            that means just the memory location, not really useful to have human readable data. so to be able to print it you must create another method.
       
                def __str__(self):
                    return f"{self.firstname} {self.lastname}" ( the f"" essentially works the same as the JS `{}` : f"{self.firstname} {self.lastname}" , `${this.firstname} ${this.lastname}`)
                        you have to make it defined then the string declaration of __str__, and have it be the self paramater, once you do that it needs to be assinged to something so thats where 
                        the colon comes in to say everyting under this colon belongs to this def __str__ (self) block, then you write out what needs printed, with a return statemnt because all functions
                        need to return something. so throw a return statement on there.
                        also all functions outside of the class must be defined at the same indentiation because theres no closing of the person class.
                            def my_function():
                                print("Hello")   # indented inside the function

                            print("Outside")     # back to original indentation

                            #this will print outside because i didn't call the my_funtion to print "hello", pretty dumb way of doing it honestly closing would make more sense

                    '''

class person :
    def __init__(self,firstname,lastname,age,country):
        self.modeled_firstname = firstname
        self.modeled_lastname = lastname
        self.modeled_age= age
        self.modeled_country = country

    def __str__(self):
        return f"{self.modeled_firstname} {self.modeled_lastname}"
            

person_two = person('hugh','jackman',203,'canada?')
person_three = person('ryan','renolds',44,'canada')



print(person_two)

#print( first_name , 'length of name: ', len(first_name))

person_info_model = {
    first_name,
    last_name,
    age,
    country,
    married
}

class Cars :
    def __init__(self, make, model,year,wheels = 4, color = 'Black'): #setting a default of 4 and color of 'unknown' as it must be set in the declaration for it to be a default not in the self.wheels = wheels = 4 XXX ignores wheels and puts 4 for every entry.
        self.make = make
        self.model = model
        self.year = year
        self.wheels = wheels 
        self.color = color

    def __str__(self):
        return f"{self.make} {self.model} Year: {self.year} Wheels: {self.wheels} Color: {self.color}"
    
car_one = Cars ('Toyota', 'Camry', 2024, 4)
car_two = Cars ('Saab', 'countache', 1994, 3, 'green')

print(car_one)
print(car_two)
        
#print( person_info_model)


def my_function():
    print("Hello")   # indented inside the function

print("Outside")     # back to original indentation
# python

my_function()

'''
Visual Cheat Sheet
| Feature                  | Python                  | JavaScript / C / Java  | Notes                         |
| ------------------------ | ----------------------- | ---------------------- | ----------------------------- |
| Block start              | Colon `:` + indentation | `{}`                   | Python uses whitespace        |
| Block end                | Dedent                  | `}`                    | Python: automatic             |
| Function definition      | `def my_func():`        | `function myFunc() {}` | Python indentation required   |
| Class definition         | `class Person:`         | `class Person {}`      | Indentation starts class body |
| Calling function         | `print("hi")`           | `console.log("hi")`    | Parentheses for call only     |
| Multiple statements/line | `x=1; y=2` (optional)   | `x=1; y=2;`            | Python discourages            |
'''

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

radius = 30
area = 0 #pie * r^2
circumfrance = 0 # 2*pie*r

area = 3.14*pow(radius, 2) 
circumfrance = 2*3.14*radius

print(f"the area of a circle with a radius of 30 is : {area}, and the circumfrance is {circumfrance}")

def findingRadius() :
    x = int(input('what is the circles radius: '))
    area = 3.14*pow(x, 2) 
    area2 = math.pi*pow(x, 2)
    area3 = round(math.pi*pow(x, 2),2)

    circumfrance = 2*3.14*x
    print(f"the area of a circle with a radius of 30 is : {area} or {area2} or {area3}, and the circumfrance is {circumfrance}")

findingRadius()