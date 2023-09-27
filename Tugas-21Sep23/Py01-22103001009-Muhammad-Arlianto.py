#1. Print The Hello World
print("Hello World")

#2. Aritmatically Create
a = 12 
b = 8
c = 2
#variabel for arimatically
d = (a + b)/c
e = c**3/b
f = b%3
print(d) #result for variable d
print(e) #result for variable e
print(f) #result for variable f

#3. Structure of logical if and else condition 
x = int(input("Input number for if and else: "))
if x >= 75:
    print(f"The largest value you choose is {x}")
elif x >= 51 and x < 75:
    print(f"The mid value you choose is {x}")
elif x <= 50 & x >= 30:
    print(f"The smallest value you choose is {x}")
else :
    print("number you choose is the pretty small number")

#4. Looping
#For Loop:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers :
    print(number)

#While Loop
num = int(input("input number for processing while looping: "))
count = 0
while count <= num:
    print(count)
    count += 1    
