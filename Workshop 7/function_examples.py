


# ใช้ global ในฟังก์ัชันอื่น
def test():
    global a, b
    a = ("ประโยคนี้ถูกสร้างในฟังก์ชัน")
    b = 10.5
    
def abc():
    print(a)
    
test()
abc()



'''
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(1000, 2000, 30))
'''
'''
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))
'''









'''
def add(f, l):
    add = f+l
    print(fNum, "+", lNum, "=", add)

def sub(f, l):
    sub = f-l
    print(fNum, "-", lNum, "=", sub)

def mul(f, l):
    mul = f*l
    print(fNum, "*", lNum, "=", mul)

def div(f, l):
    div = f/l
    print(fNum, "/", lNum, "=", round(div, 2))
    
while True:
    fNum = int(input("กรอกตัวตั้ง: "))
    lNum = int(input("กรอกตัวกระทำ: "))

    print("1. บวก | 2. ลบ")
    choice = int(input(""))
    if choice == 1:
        add(fNum, lNum)
    elif choice == 2:
        sub(fNum, lNum)
    elif choice == 3:
        mul(fNum, lNum)
    else:
        div(fNum, lNum)
'''













'''

def circle():
    value = int(input("ระบุค่ารัศมี: "))
    area = 3.14*(value*value)
    print("พื้นที่วงกลม =", area)
    
def square():
    value = int(input("ระบุค่าของด้าน: "))
    area = value*value
    print("พื้นที่สี่เหลี่ยม =", area)
    
while True:
    print("1. สี่เหลี่ยม | 2. วงกลม")
    print("ต้องการหาพื้นที่สิ่งใด: ")
    choice = int(input(""))
    if choice == 1:
        square()
    else:
        circle()

'''
    

