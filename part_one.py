
#NABATANZI GORRET SEP23/BCS/3472U/F

# PART A: 
# We have the following students details and marks: Enter these details from the keyboard
#     Student name=Ritah Liz
#     Student Number= SEP21/BCS/088U
#     Programming=78
#     Data Science= 89
#     Computer applications=55
# Calculate the average mark and print the answer in 3 decimal places.
# Display full details of the student

#Solutions
#NABATANZI GORRET SEP23/BCS/3472U/F


#Student Details
#Creating variables to store the details from the keyboard and casting the marks from string to integer
studentName = input("Enter the student's name:\t")
studentNumber = input("Enter the student's number:\t")
programmingMarks = int(input("Enter the student's marks in Programming:\t"))
dataScienceMarks = int(input("Enter the student's marks in Data Science:\t"))
computerApplicationMarks = int(input("Enter the student's marks in Computer Applications:\t"))
print("\n")


#Calculating the student's average mark scored
averageMark = (programmingMarks + dataScienceMarks + computerApplicationMarks ) / 3
#printing the average mark rounded to 3 decimal places
print(studentName + " has an Average Mark of %.3f " %averageMark + "\n"  )


#Displaying the details
print(f".....Student Details.....")
print(f"Student Name: {studentName}")
print(f"Student Number: {studentNumber}/n")
print("\n.....Student Course Unit Marks....")
print(f"Programming: {programmingMarks}")
print(f"Data Science: {dataScienceMarks}")
print(f"Computer Applications: {computerApplicationMarks} \n")

#NABATANZI GORRET SEP23/BCS/3472U/F
