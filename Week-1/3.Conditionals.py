# if elif else statement
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 86:
    print("Grade: A-")
elif marks >= 82:
    print("Grade: B+")
elif marks >= 78:
    print("Grade: B")
elif marks >= 74:
    print("Grade: B-")
elif marks >= 70:
    print("Grade: C+")
elif marks >= 66:
    print("Grade: C")
elif marks >= 62:
    print("Grade: C-")
elif marks >= 58:
    print("Grade: D+")
elif marks >= 55:
    print("Grade: D")
else:
    print("Grade: F")


#Nested
if marks > 0:
    if marks % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else: print("Negative number")

#Using Logical Operators
if marks > 0 and marks < 100:
    print("The number is between 1 and 99.")
if marks < 0 or marks > 100:
    print("The number is either negative or greater than 100.")