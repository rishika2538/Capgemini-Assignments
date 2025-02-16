#area of rectangle using input type conversion and formatted string
#username-testuser,password-Password@123 
    #you have only 3 attempts if they are failed then print no.of attempts are completed
#check the given number is prime or not
#calculate the gross salary if the salary is less than 5 lakh per annum tax is 10% else 20% 
    #display-net salary,gross salary,tax,amount
#calculate attendence tracker based on the number of classes u had 
    # if the attendence is 75% and above then u are eligible for sem exam
    # else you are not allowed to the exam

total_classes=int(input("Enter the total number of classes"))
attended_classes=int(input("Enter number of classes attended:"))
a=(attended_classes/total_classes)*100
if a>=75:
    print("You are eligible for sem exam")
else:
    print("You are not eligigble for sem exam")