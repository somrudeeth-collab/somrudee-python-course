def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_trangle_area(height, basa):
    """Calculates and displays trangle area"""
    area = 0.5 * height * basa
    print(f"Trangle with height {heigth} and basa {basa}")
    print(f"Area =  0.5  x {height} × {basa} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_trangle_area(5, 3)
calculate_trangle_area(10, 7)

"""
# เขียน FUNCTION แปลงหน่วงเงิน ที่สามารถแปลงเงินจาก
THB <--> USD ..1 USD = 32 THB
THB <--> JPY ..100 JPY = 22 THB

โดยใช้ชื่อและการใช้งาน
 function_convert_currency(100,"USD")

 แสดงผลการทำงานหน้าจอ
100 THB = 3.3 USD

และทอสอบผลการทำงาน function ที่ตัวเองเรียกด้วย
 """
def  convert_currency(a,b):
    if b =="USD":
       print(f"(a) THB = (a/ 32.0) USD"):
    else:
        print(a,"USD = ",a * 32.0,"THB"):
convert_currency (100,"USD") 
convert_currency(100,"THB") 


    
