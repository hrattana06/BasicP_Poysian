# def hello():
#     print("Hello World")

# hello()


# def add(a, b):
#     return a+b

# # ใส่ค่าไปตรงๆ
# print(add(1, 2))
# print(add(7, 100))

# # เอาตัวแปรไปใส
# x = 15
# y = 15
# result = add(x, y)
# print(result)

# def introduction(fname):
#     print("My name is", fname)

# introduction("Poysian")


# def tellAge():
#     age = input("Ernter your age :")
#     print("Your age is :", age)

# tellAge()


# def spam(x):
#     for i in range(5):
#         print(x)

# spam(5)




# x = ["pangpond", "ton", 2, 7]
# sum = x[2] + x[3]
# print(sum)

# # แก้ข้อมูลในlist
# x[2] = 3
# sum = x[2] + x[3]
# print(sum)

# x[2] = "ton"
# print(x)


# # เพิ่มข้อมูลในlist
# x = ["pangpond", "ton", 2, 7]
# print(x)
# x.append("best")
# x.append(5.2)
# print(x)

# a = 9
# x.append(a)
# print(x)

# ลบข้อมูลออกจากlist
# x = ["pangpond", "ton", 2, 7]
# x.pop(0)
# x.pop()
# print(x)


# list = ["pangpond", "ton", 2, 7, 2]
# for i in list:
#     if i == 2:
#         print("found 2")


# Dictionary
# dict_a = {
#     "sword":80,
#     "gun":70
# }
# print(dict_a["sword"])


# # เพิ่มข้อมูลใหม่/แก้ไขข้อมูลเดิม
# dict_a = {
#     "sword":80,
#     "gun":70
# }
# dict_a["sword"] = 20 # แก้ไขในdict
# print(dict_a["sword"])

# dict_a["bow"] = 35 # เพิ่มข้อมูลใหม่
# print(dict_a)


# List&Dict combination
# student = [
#     {"name":"Tom", "id":11},
#     {"name":"Tim", "id":19}
# ]
# print(student[1])




#WS
students = [
    {"name":"Pangpond", "money":400},
    {"name":"Ton", "money": 1000},
    { "name":"A", "money":300}
]

# checkMoney() เช็คเงิน>500? if yes -> rich / no -> rich less than another

def checkMoney(list):
    for student in list:
        if student["money"] > 500:
            print("เงินมาก (เงินมากกว่า 500)")
        else:
            print("เงินน้อย (เงินน้อยกว่า 500)")
        
students = [
    {"name":"Pangpond", "money":400},
    {"name":"Ton", "money": 1000},
    { "name":"A", "money":300}
]

checkMoney(students)