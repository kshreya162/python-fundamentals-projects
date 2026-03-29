studentsList=[]

while True:
    print("1.Add student details(name + marks in subjects)")
    print("2.Display all student records")
    print("3.Find topper")
    print("4. Search student by name")
    print("5. Exit")
    print("\n")

    choice=int(input("Enter your choice: "))

#adding the name and marks of the student
    if choice==1:
        name=input("Enter the name of the student:")
        marks=[]
        for i in range(1,4):
            mark=int(input(f"Marks of subject out of 100{i}: "))
            marks.append(mark)
            i=i+1

        #calculating the total and average marks
        total=0
        for i in marks:
            total+=i
        print("Total marks: ",total)

        avg_marks=total/len(marks)
        print("average marks: ",avg_marks)

        #assign grades based on average marks
        if avg_marks >= 90:
            grade="A"
        elif avg_marks >=75:
            grade="B"
        elif avg_marks >=60:
            grade="C"
        else:
            grade="D"

        student={
            "name":name,
            "marks":marks,
            "total": total,
            "average":avg_marks,
            "grade": grade
        }

        studentsList.append(student)
        print("Student added successfully!!")
        print("\n")


#displaying all students record
    elif choice==2:
        if len(studentsList)==0:
            print("No students added!")
        else:
            count=1
            for items in studentsList:
                print(f"Student number {count}\nName of the student:{items['name']}\nMarks:{items['marks']}\nTotal Marks:{items['total']}\nAvg Marks:{items['average']}\nGrade:{items['grade']}\n")
                count+=1

#finding the topper among the students
    elif choice==3:
        if len(studentsList)==0:
            print("No students added!")
        else:
            topper=studentsList[0]
            for i in studentsList:
                if i['average'] > topper["average"]:
                    topper= i
            
            print("Topper name: ",topper['name'])
            print("Average marks of topper:",topper['average'])
            print("\n")

#searching student by name
    elif choice==4:
        if len(studentsList)==0:
            print("No students added!")
        else:
            search_name=input("Enter the name to search: ")
            found=False
            for i in studentsList:
                if i['name'] == search_name:
                    print("Student found!!")
                    print(i)
                    found=True
            if not found:
                    print("Student not found!!")
        print("\n")
    elif choice==5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")



        