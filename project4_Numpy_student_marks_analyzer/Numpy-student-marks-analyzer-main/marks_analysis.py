import numpy as np

marks=np.array([
    [85, 90, 78],
    [92, 88, 95],   
    [76, 80, 82],
    [89, 94, 91],
])

avg_marks=np.mean(marks,axis=1)

highest_marks = np.max(marks,axis=1)
lowest_marks = np.min(marks,axis=1)

updated_marks = marks + 5

high_performers= avg_marks > 90

print("Average Marks:", avg_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Updated Marks:\n", updated_marks)
print("High Performers above 90 avg:", high_performers)

