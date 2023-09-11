 #Temperature convesion
print("TEMPERATUE CONVERSION")  #menu print for the user
print("1.Celcius to Farenheit")
print("2.Farenheit to Celcius")
c=int(input("enter the choice"))
if c==1:
    cel=float(input("Enter temperature in celcius"))
    f=cel*9/5+32
    print("Temperature in Farenhiet is",f)
elif c==2:
    far=float(input("Enter temperature in Farenheit"))
    celc=(far-32)*5/9
    print("Temperature in celcius is",celc)
else:
    print("you entered a wrong choice")