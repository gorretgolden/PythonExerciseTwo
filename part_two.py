#NABATANZI GORRET SEP23/BCS/3472U/F

#Question 1
#Write a program that converts celsius temperature to Fahrenheit.The program should ask the user to enter the
# temperature in celsius and then display the temperature converted to Fahrenheit


#store celicius value from the user
print("\n*** Celicius to Farenheit Degrees Conversion ***\n")
celicius = input('Enter the Temperature in Celicius Degerees: ')
F = (9/5) * int(celicius) + 32 #Conversion Expression
fahreneit = int(F) #casting the expression to a float type
print(celicius + " Degrees Celicius is equal to " + str(fahreneit) + " Degrees Farenheit\n")


#NABATANZI GORRET SEP23/BCS/3472U/F
#Question 2
#A car's miles per gallaton can be calculated with the following formula. Write a program that asks the user
#for the number of miles driven and gallons used. It should calculate the car's miles-per-gallons-used and display the 
#result
#MPG = milesDriven / gallonsOfGasUsed

print("\n*** Car's Miles Per Gallon Calculations ***\n")

#storing user input and casting it to type float
milesDriven = float(input('Enter the number of miles driven: '))
gallonsOfGasUsed = float(input('Enter the number of gallons of gas used: '))
MPG =  milesDriven / gallonsOfGasUsed
milesPerGallons = MPG
#displaying the car's miles per gallons used
print("The car has used %.2f" %milesPerGallons + " miles per gallons")



#NABATANZI GORRET SEP23/BCS/3472U/F
#Question 3
#The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 5. 
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

print("\n*** Calculating the Volume of a Sphere ***\n")

#storing the radius from the keyboard and casting it to int
radius = int(input('Enter the radius of the sphere: '))
volumeOfSphere = float((4/3) * 3.14 * radius ** 2)
print("The volume of a sphere with radius " + str(radius) + " is %.2f " %volumeOfSphere )


