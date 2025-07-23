monster = 100
stick = 10
book = 20
sword = 30


while True:
    print("ต่อสู้กับมอนเตอร์หรือไม่")
    print("1.สู้")
    print("2.ออก")
    choice = int(input("คุณเลือก : "))
    if choice == 2:
        print("คุณออกจากเกม")
        break
    elif choice == 1:
        print("เล่นต้องการเล่น")
        no = int(input("ผู้เล่นต้องการเล่นกี่รอบ"))
        for i in range (no):