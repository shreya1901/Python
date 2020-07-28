from math import pi
r=float(input('Please Enter Radius of circle = '))
a=pi*r**2
print("Area of circle is " + str(a))
file_Name=input("Enter File Name = ").casefold()
b=file_Name.split('.')
y=b[1]
if(y=='py'):
    print("File extention is python")
elif(y=='java'):
    print("File extention is java")
elif(y=='cpp'):
    print("File extention is c++")
elif(y=='c'):
    print("File extention is c")
else:
    print("Input is out of range, Please Enter valid Input")
