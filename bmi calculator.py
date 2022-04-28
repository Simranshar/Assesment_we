Name= input("enter your name")
Gender = input("enter your gender")
Age = float(input("your age"))
Weight =float(input("your weight"))
Height =float(input("enter your height in m"))
BMI=float((Weight)/(Height* Height))
print(BMI)
if Gender=="female":
    if BMI<18.5:
        print("underweight")
    elif 18.5<BMI<24.9:
        print("normal")
    elif 25<BMI<29.9:
        print("overweight")
    else:
        print("obese")
if Gender=="male":
    if BMI<18.5:
        print("underweight")
    elif 18.5<BMI<25.9:
        print("normal")
    elif 25.9<BMI<29:
        print("overweight")
    else:
        print("obese")
else:
    print("revise the entered data")