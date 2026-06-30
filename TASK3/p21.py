# List

students = ["Sam", "Raj", "Aman"]

students.append("Rohan")
students.insert(1, "Karan")
students.remove("Raj")

print(students)
print("Total Students:", len(students))

# Tuple

college = ("Chetana", "Nagpur", 2026)

print(college.index("Nagpur"))
print(college.count(2026))

# Set

skills = {"Python", "Git", "Python", "AI"}

skills.add("ML")
skills.remove("Git")

skills2 = {"AI", "Cyber Security"}

print("Union:", skills.union(skills2))
print("Intersection:", skills.intersection(skills2))