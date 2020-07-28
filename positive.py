list=[]
list1=[]
n= int(input("Enter total number of element you want to enter in your list : "))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
#checking positive number
for num in list:
    if num>=0:
        list1.append(num)
print("positive numbers are",list1)
