print("=== 1. STUDENT DETAILS (TUPLE) ===")
student_details = ("STD-8042", "Kanishk", "Grade 8", "Lincoln High School")

print(f"Student ID   : {student_details[0]}")
print(f"Student Name : {student_details[1]}")
print(f"Grade        : {student_details[2]}")
print(f"School       : {student_details[3]}")
print("-" * 45)


print("\n=== 2. SUBJECT SETS & MODIFICATIONS ===")

monday_subjects = {"Math", "English", "Science", "History"}
tuesday_subjects = {"Math", "Science", "Computer Science", "Art"}

print(f"Initial Monday Subjects : {monday_subjects}")
print(f"Initial Tuesday Subjects: {tuesday_subjects}")

monday_subjects.add("Physical Education")
print(f"\nAfter adding 'Physical Education' to Monday:")
print(monday_subjects)

tuesday_subjects.remove("Art")
print(f"\nAfter removing 'Art' from Tuesday:")
print(tuesday_subjects)

print("-" * 45)


print("\n=== 3. SUBJECT COMPARISONS (SET OPERATIONS) ===")

common_subjects = monday_subjects & tuesday_subjects
print(f"Common subjects (Monday & Tuesday): {common_subjects}")

all_unique_subjects = monday_subjects | tuesday_subjects
print(f"All unique subjects taught this week: {all_unique_subjects}")

monday_only = monday_subjects - tuesday_subjects
print(f"Subjects taught ONLY on Monday: {monday_only}")

tuesday_only = tuesday_subjects - monday_subjects
print(f"Subjects taught ONLY on Tuesday: {tuesday_only}")

different_subjects = monday_subjects ^ tuesday_subjects
print(f"Subjects not shared between days: {different_subjects}")