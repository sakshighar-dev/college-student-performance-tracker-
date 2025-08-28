import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

# Load data
df = pd.read_csv("C:/Users/saksh/OneDrive/Desktop/student_data.csv")
df['Roll No'] = df['Roll No'].astype(str).str.lower()
df['Name'] = df['Name'].str.lower()

# Function to search and display student info
def search_student():
    search = entry.get().strip().lower()
    if search == "":
        messagebox.showwarning("Input Error", "Please enter Roll No or Name.")
        return

    student = df[(df['Roll No'] == search) | (df['Name'] == search)]

    output.delete(1.0, tk.END)

    if student.empty:
        output.insert(tk.END, "❌ Student not found.\n")
    elif len(student) > 1:
        output.insert(tk.END, "👥 Multiple students found:\n")
        for _, row in student.iterrows():
            output.insert(tk.END, f" - {row['Name'].title()} (Roll No: {row['Roll No'].upper()})\n")
    else:
        student = student.iloc[0]
        output.insert(tk.END, f"\n📄 Student Report: {student['Name'].title()} (Roll No: {student['Roll No'].upper()})\n\n")

        marks = [student['Sem1 Marks'], student['Sem2 Marks'], student['Sem3 Marks'], student['Sem4 Marks']]
        grades = [student['Sem1 Grade'], student['Sem2 Grade'], student['Sem3 Grade'], student['Sem4 Grade']]

        output.insert(tk.END, "📚 Semester-wise Marks & Grades:\n")
        for i in range(4):
            output.insert(tk.END, f"   - Sem {i+1}: {marks[i]} Marks, Grade: {grades[i]}\n")

        total = sum(marks)
        avg = total / 4

        output.insert(tk.END, f"\n📈 Total Marks: {total}")
        output.insert(tk.END, f"\n📊 Average: {round(avg, 2)}")

        # Performance status
        if avg >= 440:
            status = "Topper 💥"
            comment = "Outstanding performance!"
        elif avg >= 400:
            status = "Above Average ⭐"
            comment = "Very good academic record."
        elif avg >= 350:
            status = "Average ✅"
            comment = "Decent but can improve."
        else:
            status = "Below Average ⚠"
            comment = "Needs improvement."

        output.insert(tk.END, f"\n\n🎯 Performance: {status}")
        output.insert(tk.END, f"\n\n💼 Projects Done:\n")
        output.insert(tk.END, f"   1. {student['Project 1']}\n")
        output.insert(tk.END, f"   2. {student['Project 2']}\n")
        output.insert(tk.END, f"\n✅ Final Remark: {comment}")
        output.insert(tk.END, "\n" + "-"*60 + "\n")

# GUI Setup
root = tk.Tk()
root.title("🎓 Student Performance Tracker")
root.geometry("700x600")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="🔍 Enter Roll No or Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry = tk.Entry(frame, width=40, font=("Arial", 12))
entry.grid(row=0, column=1, padx=5)

search_btn = tk.Button(frame, text="Search", command=search_student, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
search_btn.grid(row=0, column=2, padx=5)

output = scrolledtext.ScrolledText(root, width=80, height=30, font=("Consolas", 10))
output.pack(pady=10)

root.mainloop()
