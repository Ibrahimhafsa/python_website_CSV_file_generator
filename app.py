import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator📁")

names = ["Ali", "Hafsa", "Jaweriya", "Saad", "Uzair", "Hasnain", "Ummehani",
"Mantasha", "Zahra", "Muhib", "Musab", "Saif", "Arham", "Zain" ]

students = []
for i in range(1, 14):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generated Students Data📚")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")
st.success("Students Record Generated Successfully!🎉")