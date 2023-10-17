while True:
    def circle():
        radius = int(input("ระบุรัศมี: "))
        area = 3.14*(radius*radius)
        print("พื้นที่วงกลม =", area)

    def triangle():
        base = int(input("ระบุความยาวฐาน: "))
        height = int(input("ระบุความสูง: "))
        area = 0.5*(base*height)
        print("พื้นที่สามเหลี่ยม =", area)

    def rectangular():
        width = int(input("ระบุความกว้าง: "))
        height = int(input("ระบุความยาว: "))
        area = width*height
        print("พื้นที่สี่เหลี่ยม =", area)
    
    print("ระบุรูปทรงที่ต้องการคำนวณ")
    choice = int(input("1=วงกลม, 2=สามเหลี่ยม, 3=สี่เหลี่ยม: "))

    if choice == 1:
        circle()
    elif choice == 2:
        triangle()
    elif choice == 3:
        rectangular()

