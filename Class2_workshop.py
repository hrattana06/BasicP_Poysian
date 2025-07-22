
way = int(input("ระยะทาง : "))
print(way)
if way >=5 and way <=50:
    print("ราคา 10 บาท")
elif way >=51 and way <=100:
    print("ราคา 15 บาท")
elif way >=101 and way <=300:
    print("ราคา 30 บาท")
elif way >=301 and way <=500:
    print("ราคา 35 บาท")
elif way >500:
    print("ราคา 45 บาท")
else:
    print("ไม่ไปส่ง")