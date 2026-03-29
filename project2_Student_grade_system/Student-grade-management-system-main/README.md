Student Grade Management System

📌 Project Overview

This is a simple console-based Python application designed to manage student records. The system allows users to add student details, calculate performance metrics, and retrieve information efficiently.

The project is built strictly using basic Python constructs:

- Loops
- If-else statements
- Lists
- Dictionaries

No user-defined functions or file handling are used.

---

🎯 Features

- Add student details (name and marks)
- Calculate total and average marks
- Assign grades automatically
- Display all student records
- Identify the class topper
- Search for a student by name

---

🛠️ Technologies Used

- Python (Core concepts only)

---

📊 Grading Criteria

| Average Marks | Grade |
| ------------- | ----- |
| ≥ 90          | A     |
| ≥ 75          | B     |
| ≥ 60          | C     |
| < 60          | D     |

---

🚀 How to Run the Project

1. Install Python (version 3.x recommended)
2. Copy the code into a `.py` file 
3. Open terminal or command prompt
4. Run the program:

---

🧭 Menu Options

When you run the program, you will see the following menu:

1. Add Student
2. Display All Students
3. Find Topper
4. Search Student
5. Exit

Enter the corresponding number to perform an action.

---

📦 Data Structure Used

Each student is stored as a dictionary:


{
  "name": "Student Name",
  "marks": [marks1, marks2, marks3],
  "total": total_marks,
  "average": avg_marks,
  "grade": "A/B/C/D"
}


All student records are stored inside a list:


students = []


---

⚙️ Program Logic

- Uses loops to repeatedly show menu options
- Uses lists to store multiple student records
- Uses dictionaries to structure student data
- Uses conditional statements to assign grades and process logic

---

⚠️ Limitations

- Data is not saved permanently (no file handling)
- No graphical user interface (console only)
- Fixed number of subjects (3 subjects)

---

🔄 Future Enhancements

- Add file/database storage
- Implement user-defined functions for better structure
- Add more subjects dynamically
- Sort students by performance
- Build a GUI version using Tkinter or web technologies

---

📚 Learning Outcomes

Understanding of loops and control flow
- Practical use of lists and dictionaries
- Basic problem-solving and logic building
- Structuring a small real-world application

---

👩‍💻 Author

Student Project – Beginner Level Python

---
