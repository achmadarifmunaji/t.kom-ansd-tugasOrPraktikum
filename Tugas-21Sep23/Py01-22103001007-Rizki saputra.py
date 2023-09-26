#1. Cetak Hello World
print("Hello World")

#2. Variable dan operasi matematika
'''a,b dan c adalah variabel,
10,2 dan 3 adalah nilai dari variabel'''
a = 10 
b = 2
c = 3
print(a+b+c) #operasi matematika penjumlahan
print(a*b*c) #operasi matematika perkalian
print(a-b-c) #operasi matematika pengurangan

#3. Struktur pengkondisian (If-Else)
x = 10
if x > 5:
    print("x lebih besar dari 5")
else :
    print("x tidak lebih besar dari 5")

#4. Looping (Perulangan)
#For Loop:
'''mengulangi kode sebanyak jumlah
element dalam suatu list'''
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits :
    print(fruit)

#While Loop
'''mengulangi kode selama kondisi
yang di berikan masih benar'''
i = 0
while i < 5:
    print(i)
    i += 1