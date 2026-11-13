import webbrowser

students = [
    {
        "Student ID": "24/13809",
        "Department": "Computer Science",
        "Level": 200,
        "Attendance Percentage": 85,
        "Average Examination Score": 78
    },
    {
        "Student ID": "24/14728",
        "Department": "Cyber Security",
        "Level": 200,
        "Attendance Percentage": 90,
        "Average Examination Score": 82
    },
    {
        "Student ID": "24/16902",
        "Department": "Computer Science",
        "Level": 300,
        "Attendance Percentage": 75,
        "Average Examination Score": 69
    },
    {
        "Student ID": "24/14578",
        "Department": "Software Engineering",
        "Level": 100,
        "Attendance Percentage": 95,
        "Average Examination Score": 88
    },
    {
        "Student ID": "24/13456",
        "Department": "Cyber Security",
        "Level": 300,
        "Attendance Percentage": 80,
        "Average Examination Score": 74
    }
]

student_details = {
    "Name": "Nwosu Rejoice Amarachi",
    "Matric Number": "24/13713",
    "Department": "Computer Science",
    "Course Code": "CUL-CYB 371",
    "Level": "300"
}

rows = ""
for student in students:
    rows += f"""
    <tr>
        <td>{student["Student ID"]}</td>
        <td>{student["Department"]}</td>
        <td>{student["Level"]}</td>
        <td>{student["Attendance Percentage"]}%</td>
        <td>{student["Average Examination Score"]}</td>
    </tr>
    """

student_details_html = "".join(
    f"<p><strong>{key}:</strong> {value}</p>" for key, value in student_details.items()
)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Dataset Table</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: linear-gradient(135deg, #eaf3ff 0%, #f7f9fc 100%);
            color: #1f2937;
        }}
        h2, h3 {{
            color: #0f4c81;
            margin-bottom: 12px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background: white;
            box-shadow: 0 8px 20px rgba(15, 76, 129, 0.12);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 25px;
        }}
        th, td {{
            padding: 14px 16px;
            text-align: left;
            border-bottom: 1px solid #dfeaf7;
        }}
        th {{
            background: linear-gradient(135deg, #8b5cf6, #7c3aed);
            color: white;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background-color: #f8f3ff;
        }}
        tr:hover {{
            background-color: #ede9fe;
        }}
        .student-card {{
            background: white;
            padding: 20px 24px;
            box-shadow: 0 8px 20px rgba(91, 33, 182, 0.1);
            border-radius: 12px;
            margin-top: 20px;
            border-left: 6px solid #10b981;
        }}
        .student-card p {{
            margin: 8px 0;
            color: #374151;
        }}
    </style>
</head>
<body>
    <h2>Student Performance Dataset</h2>

    <table>
        <thead>
            <tr>
                <th>Student ID</th>
                <th>Department</th>
                <th>Level</th>
                <th>Attendance %</th>
                <th>Avg Exam Score</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>

    <div class="student-card">
        <h3>Student Details</h3>
        {student_details_html}
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("HTML report created: index.html")
webbrowser.open("index.html")
