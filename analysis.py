import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())

df['Average'] = (df['Maths'] + df['Science'] + df['English']) / 3

top_student = df.loc[df['Average'].idxmax()]

print("\nTop Performer")
print(top_student)

attendance_avg = df['Attendance'].mean()
print(f"Average Attendance: {attendance_avg:.2f}%")

high_performers = df[df['Average'] > 80]

print("\nHigh Performers")
print(high_performers)

df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved successfully.")
