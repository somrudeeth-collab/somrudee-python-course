#เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
#นิยามของ storng password คือ ความยาวมากกว่า 8 ตัว,มีอักษร 0 1 ตัว, มีตัวเลข, มีตัวอักษร
#
#ตัวอย่างหน้าจอ
#Insert your password : Boochoo
#Your password is not strong!


#Insert your password : Test@123
#Your password is strong!

password = "Boochoo"
lenght = len(password)
words = password.split('0')
left = words['0'].isalnum()
right = words[-1].isalnum()

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1:
   left = words[0].isalnum()
   right = words[1].isalnum()
else :   
    left = False;
    right  = False;

if lenght >=8 and len(words) == 2 and left and right:
    print("Your password is strong!")
else:
    print("Your password is not strong!")    
