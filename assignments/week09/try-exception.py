# ERROR (bogs) 
# 3 types => svntax errors / runtime error / logic error
 

#ValueError Exception
try:
    age = int(input("กรอกอายุ:"))
    print (f"ปีหน้าคุณจะอายุ {age+-1}ปี")
except ValueError:
    print ("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")


#ZeroDivisionException:
try:
    numrator = float(input("กรอกตัวตั้ง:"))
    denominator = float(input("กรอกตัวหาร:"))

    result = numrator / denominator
    print (f"ผลลัพธ์ = {result}")

except ValueError :
    print = ("กรุณากรอกตัวเลขให้ถูกต้อง")


except ZeroDivisionError:
    print = ("ไม่สามารถหารศูนย์ได้") 


#FileNotFoundException , PermissionException
try:
    filename = input("ชื่อไฟล์:")
    with open(filename, "r" , rncoding="ut-8")as file:
         content = file.read()

    print("เนื้อหาในไฟล์:")
    print(content)

except FileNotFoundError:
    print(f"ไม่พบไฟล์ชื่อ{filename}")
except PermissionError:
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")


try:
    score=float(input("กรอกคะแนน 0-100:"))

    if not 0 <= score <= 100: 
    raise ValueError ("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง :{error}")

else:
    print(f"บันทึงคะแนน {score}เรียบร้อย")

finally:
    print("จบการตรวจสอบคะแนน")



