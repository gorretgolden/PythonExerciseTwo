#NABATANZI GORRET SEP23/BCS/3472U/F

#PART ONE
#Write a program that converts celicius to faranheit.The program should ask the user to enter the
# temperature in celicus and then display the temperature converted to Farenheit

#Conversion Expression

#store celicius value from the user
print("\n*** Celicius to Farenheit Degrees Conversion ***\n")
celicius = input('Enter the Temperature in Celicius Degerees: ')
F = (9/5) * int(celicius) + 32
faranheit = float(F) #casting the expression to a float type
print(celicius + " Degrees Celicius is equal to " + str(faranheit) + " Degrees Farenheit\n")


#NABATANZI GORRET SEP23/BCS/3472U/F
#PART TWO
#A car's miles per gallaton can be calculated with the following formula. Write a program that asks the user
#for the number of miles driven and gallons used. It should calculate the car's miles-per-gallons-used and display the 
#result
#MPG = milesDriven / gallonsOfGasUsed

print("\n*** Car's Miles Per Gallon Calculations ***\n")
#storing user input and casting them to type int
milesDriven = int(input('Enter the number of miles driven: '))
gallonsOfGasUsed = int(input('Enter the number of gallons of gas used: '))
MPG =  float(milesDriven / gallonsOfGasUsed)
milesPerGallons = MPG
#displaying the car's miles per gallons used
print(f"The car has used {milesPerGallons} miles per gallons")


