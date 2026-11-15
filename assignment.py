students = [
    {
        "student_id": "24/13809",
        "department": "Computer Science",
        "level": 200,
        "attendance_percentage": 85,
        "avg_exam_score": 78,
    },
    {
        "student_id": "24/14728",
        "department": "Cyber Security",
        "level": 200,
        "attendance_percentage": 90,
        "avg_exam_score": 82,
    },
    {
        "student_id": "24/16902",
        "department": "Computer Science",
        "level": 300,
        "attendance_percentage": 75,
        "avg_exam_score": 69,
    },
    {
        "student_id": "24/14578",
        "department": "Software Engineering",
        "level": 100,
        "attendance_percentage": 95,
        "avg_exam_score": 88,
    },
        {
        "student_id": "24/13456",
        "department": "Cyber Security",
        "level": 300,
        "attendance_percentage": 80,
        "avg_exam_score": 74,
    },
]

print("Student Performance Dataset")
print("Student ID | Department       | Level | Attendance % | Avg Exam Score")
print("-" * 72)

for student in students:
    print(
        f"{student['student_id']:<10} | "
        f"{student['department']:<16} | "
        f"{student['level']:<5} | "
        f"{student['attendance_percentage']:<12} | "
        f"{student['avg_exam_score']}"
    )

