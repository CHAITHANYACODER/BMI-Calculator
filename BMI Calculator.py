Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight please take care of your health eat health food and drinks more water")
	elif(BMI<=18.5):
		print("you are underweight Please take care of it and eat well and drinks more water")
	elif(BMI<=25):
		print("you are Healthy but regular workouts helps improve overall health" )
	elif(BMI<=30):
		print("you are overweight please take care of it and do workouts")
	else: print("you are severely overweight please take care of it")
else:("enter valid details")