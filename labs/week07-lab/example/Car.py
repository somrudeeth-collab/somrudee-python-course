class Car:
    # Class attribute (shared by all instances)
    wheels = 4 
    vehicle_type = "Car" #ประเภทของวัตถุ
    
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 #รถทุกคันจะต้องมีข้อมูล ยี่ห้อ,ระยะทาง,ปี ซื้อรถมารถจะค่าเท่ากับ0 มี4เดต้า
    
    def drive(self, distance):
        """Method to update mileage"""
        self.mileage += distance
        return f"Drove {distance} km. Total mileage: {self.mileage} km"
    # รถออกจากศูนย์ 0+50=50 ระยะทางเพิ่มระยะทางเก่าไปใหม่

    def get_info(self):
        """Method to get car information"""
        return f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km"
    #พ้นข้อความข้อมูลของรถนั้นๆ

    @classmethod 
    def get_vehicle_type(cls):
        """Class method to access class attributes"""
        return cls.vehicle_type

# Creating instances==>สร้างวัตถุจากคลาส
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accessing class attributes
print(f"All cars have {Car.wheels} wheels")
print(f"Vehicle type: {Car.get_vehicle_type()}")

# Accessing instance attributes
print(car1.get_info()) #พ้นข้อความ
print(car2.get_info())

# Using methods
print(car1.drive(100)) #ขับ100โล จาก0-100
print(car2.drive(250)) 

print(car1.drive(200)) #พ้นข้อความ ออกรถมา0แต่เราขับไปแล้ว 100 ขับอีก200เป็น 300โล
