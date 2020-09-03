# Author: Lauren Hughes lmh5981@psu.edu
Fgrade = input("Enter your course 1 letter grade: ")
Fcredit = input("Enter your course 1 credit: ")
if Fgrade == "A":
  gradepoint1 = 4.0
elif Fgrade == "A-":
  gradepoint1 = 3.67
elif Fgrade == "B+":
  gradepoint1 = 3.33
elif Fgrade == "B":
  gradepoint1 = 3.0
elif Fgrade == "B-":
  gradepoint1 = 2.67
elif Fgrade == "C+":
  gradepoint1 = 2.33
elif Fgrade == "C":
  gradepoint1 = 2.0
elif Fgrade == "D":
  gradepoint1 = 1.0
else:
  gradepoint1 = 0.0
print(f"Grade point for course 1 is: {gradepoint1}")
Sgrade = input("Enter your course 2 letter grade: ")
Scredit = input("Enter your course 2 credit: ")
if Sgrade == "A":
  gradepoint2 = 4.0
elif Sgrade == "A-":
  gradepoint2 = 3.67
elif Sgrade == "B+":
  gradepoint2 = 3.33
elif Sgrade == "B":
  gradepoint2 = 3.0
elif Sgrade == "B-":
  gradepoint2 = 2.67
elif Sgrade == "C+":
  gradepoint2 = 2.33
elif Sgrade == "C":
  gradepoint2 = 2.0
elif Sgrade == "D":
  gradepoint2 = 1.0
else:
  gradepoint2 = 0.0
print(f"Grade point for course 2 is: {gradepoint2}")
Tgrade = input("Enter your course 3 letter grade: ")
Tcredit = input("Enter your course 3 credit: ")
if Tgrade == "A":
  gradepoint3 = 4.0
elif Tgrade == "A-":
  gradepoint3 = 3.67
elif Tgrade == "B+":
  gradepoint3 = 3.33
elif Tgrade == "B":
  gradepoint3 = 3.0
elif Tgrade == "B-":
  gradepoint3 = 2.67
elif Tgrade == "C+":
  gradepoint3 = 2.33
elif Tgrade == "C":
  gradepoint3 = 2.0
elif Tgrade == "D":
  gradepoint3 = 1.0
else:
  gradepoint3 = 0.0
print(f"Grade point for course 3 is: {gradepoint3}")
gradepoint1 = float(gradepoint1)
gradepoint2 = float(gradepoint2)
gradepoint3 = float(gradepoint3)
Fcredit = int(Fcredit)
Scredit = int(Scredit)
Tcredit = int(Tcredit)
GPA = ((gradepoint1*Fcredit)+(gradepoint2*Scredit)+(gradepoint3*Tcredit))/(Fcredit+Scredit+Tcredit)
print(f"Your GPA is: {GPA}")