# operators
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2
print('Exponentiation: ', 2 ** 4)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (4 + 1j)) #not the same as factoring

# Write a script that prompts the user to enter base and height of the triangle 
# and calculate an area of this triangle (area = 0.5 x b x h).

base1 = int (input('enter base: '))
height1 = int (input('enter height: '))
areaOfTriange1 = (.5*base1*height1)
print(f"The area of your Triangle is : {areaOfTriange1}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

print('=========== finding perimeter ===============')
A = int(input('Enter side A: '))
B = int(input('Enter side B: '))
C = int(input('Enter side C: '))
Perimeter1 = A+B+C
print(f"The perimeter of the triangle is {Perimeter1}")

def triangle():
    base = int (input('enter base: '))
    height = int (input('enter height: '))
    sideA = int(input('Enter side A: '))
    sideB = int(input('Enter side B: '))
    sideC = int(input('Enter side C: '))
    print('=========== finding Area ===============')
    areaOfTriange = (.5*base*height)
    print(f"area = {areaOfTriange}")
    print('=========== finding perimeter ===============')
    Perimeter = sideA+sideB+sideC
    print(f"Perimeter = {Perimeter}")

triangle()


#print(365*24*60*60*100)
