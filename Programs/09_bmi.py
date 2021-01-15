weight=float(input("What is your weight ?\n"))
height=float(input("what is your height in m ?\n"))
bmi=round(weight/(height**2))
new_bmi=str(bmi)
if bmi<18.5:
    print("Your bmi is "+new_bmi+"You are underweight")
elif bmi<25:
       print("Your bmi is "+new_bmi+"You are normal")
elif bmi<30:
    print("Your bmi is "+new_bmi+"You are overweight")      
elif bmi<35:
    print("Your bmi is "+new_bmi+"You are obese") 
else:
    print("You have to meet doctor bitch you have eaten much more !!")
