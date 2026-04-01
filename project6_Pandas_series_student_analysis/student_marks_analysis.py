#Problem Statement: You have marks of students in a class. Perform analysis using Pandas Series.

import pandas as pd

#creating 2 series
student_marks = pd.Series([85, 90, 78, 92, 85, 76, 90, None, 88, 76], index=range(1,11), name="Marks")
student_names = pd.Series(["Amit","Neha","Raj","Riya","Amit","John","Neha","Karan","Pooja","John"], index=range(1,11), name="Name")

print(student_marks)
print(student_names)

print("Total students: ",len(student_marks))
print("Datatype of marks: ",student_marks.dtype)
print("Index Labels: ",student_marks.index)

print("number of missing values: ", student_marks.isnull().sum())
avg_marks= student_marks.mean()
student_marks= student_marks.fillna(avg_marks)
print("Replacing missing values with average marks:\n",student_marks)

print("Highest marks obtained in the class: ",student_marks.max())
print("Lowest marks obtained in the class: ",student_marks.min())
print("Average marks of the class: ",student_marks.mean())
print("Total sum of all marks: ",student_marks.sum())

print("Student who scored more than 85:\n")
print(
pd.concat([student_names[student_marks > 85], student_marks[student_marks > 85]],axis=1))
print()
print("Student who scored less than 80:\n")
print(
pd.concat([student_names[student_marks < 80], student_marks[student_marks < 80]],axis=1))

print("Frequency of each value: ",student_marks.value_counts())

print("Unique students names: ", student_names.unique())
print("Number of unique students: ",student_names.nunique())

student_marks= student_marks.apply(lambda x: x+5)
print(student_marks)

category=student_marks.apply(
    lambda x: "Excellent" if x >= 90
    else "Good" if x >= 80 
    else "Average"
)
category.name ="Performance"

print(category)

print("Ascending order:\n",student_marks.sort_values())
print()
print("Descending order:\n",student_marks.sort_values(ascending=False))
print()

combination=pd.concat([student_names,student_marks,category],axis=1)
print(combination)


