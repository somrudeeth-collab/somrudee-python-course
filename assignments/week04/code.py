# ป้อนชื่อจริง (หรือข้อความ) จากผู้ใช้
# ป้อนจำนวนสระทั้งหมดในข้อความนี้มีกี่ตัว (a , e , i , o, u )
# โดยต้องใช้ loop-for  ด้วยเท่านั้น

# What is your name?: Boonchoo
# Your text 4 vowels

name = input ("what is your name?:")
letters = list ("name")
print(letters)
a = letters.count ("a")
e = letters.count ("e")
i = letters.count ("i")
o = letters.count ("o")
u = letters.count ("u")

A = letters.count ("A")
E = letters.count ("E")
I = letters.count ("I")
O = letters.count ("O")
U = letters.count ("U")

count = a + e +  i +  0 + u + A + E + I + U


count = 0
for letters in name:
    if letters == 'a' or letters == 'A':
       count == count +1
    if letters == 'e' or letters == 'E':
       count == count +1
    if letters == 'i' or letters == 'I':
       count == count +1
    if letters == 'o' or letters == 'O':
       count == count +1
    if letters == 'u' or letters == 'U':
       count == count +1 

         
count = 0
if letters in [ 'a ','e','i','o','u','A','E','I','O','U']:
       count == count +1

       #print (f "ตัวอักษร {letters}"):

print("Your text have ,count, "vowels""):
    
