height=int(input("What is your height in cm "))

if height>120:
    print("you are eligible")
    age=int(input("What is your age?"))
    if age<18:
        print("Your ticket is 7$")
    if age>18:
        print("your ticket is 12$")    
else:
    print("You are not eligible Groww up!!")
