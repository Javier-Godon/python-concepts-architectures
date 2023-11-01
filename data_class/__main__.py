from data_class.Device import DeviceClass, DeviceDataClass

phone1 = DeviceClass("Note 10", "Samsung", 1_000, 2020)
phone2 = DeviceClass("Note 10", "Samsung", 1_000, 2020)
phone3 = DeviceClass("14", "Iphone", 1_200, 2020)

print(phone1)
print(id(phone1))
print(id(phone2))
print(phone1 == phone2)
# print(phone3 > phone2)

phone4 = DeviceDataClass("Note 10", "Samsung", 1_000, 2020)
phone5 = DeviceDataClass("Note 10", "Samsung", 1_000, 2020)
phone6 = DeviceDataClass("14", "Iphone", 1_200, 2020)

print(phone4)
print(id(phone2))
print(id(phone5))
print(phone4 == phone5)
print(phone6 > phone5)
