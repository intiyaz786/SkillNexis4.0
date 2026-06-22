import csv

print("Student Email List")
print("-" * 30)

with open("students.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        name=row["Name"]
        email=row["Email"]

        subject="Python Internship Update"

        message=f"""
Hello {name},

Congratulations!

You have been selected for the Python Internship Program.

Best Regards,
Training Team
"""

        print("To:",email)
        print("Subject:",subject)
        print(message)
        print("-" * 30)

print("All emails processed successfully!")
