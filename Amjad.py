'''developed by Alrazi
TP07837
'''
'''Q1'''
print('Welcome to student registration system \n 1.Register\n2.Update\n3.Delete\n4.Exet')
'''Q2'''
name=input("Please enter your name:")
TP=input("Please enter your TP number:")
Marks=int(input("Plese enter your marks:"))
CGPA=int(input("Plese enter your CGPA:"))
print("Name:",name)
print("TP Number:", TP)
print("Marks:",Marks)
print("CGPA:",CGPA)
'''Q3'''
x=float(input("Please enter nummber 1:"))
y=float(input("Please enter number 2:"))
sum=x+y
print("Sum:",sum)
Difference=x-y
print('Difference:',Difference)
P=x*y
print("product:",P)
Q=x/y
print("Quotient",Q)
'''Q4'''
m=float(input("Enter your value by meter: "))
Km= m / 1000
print(" your Value is",Km,"Km")
'''Q5'''
F=float(input("Enter F temperature:"))
C=5.0/9.0 *(F-32)
print("Your F tempreture is equals to ",round(C,3))
print("have a nice day")
'''Q6'''
import math

r=float(input('Please enter radius:'))
h=float(input("Please enter height:"))
V=float(math.pi*r**2*h)
L=float(2*math.pi*h*r)
T=float(2*math.pi*r*(r+h))
print("Volume for the circular cylinder is:",round(V,3))
print("Lateral surface area is:",round(L,3))
print("Total surface area is:",round(T,3))
