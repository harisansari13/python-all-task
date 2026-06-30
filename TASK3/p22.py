# List

members = ["Sam", "Raj", "Aman"]

members.append("Rohan")
members.insert(1, "Karan")
members.pop()
members.sort()

print("Members:", members)

# Tuple

club_info = ("Gamers Club", "Nagpur", 2026)

print("Count:", club_info.count("Nagpur"))
print("Index:", club_info.index("Nagpur"))

# Set

skills1 = {"Python", "Gaming", "AI"}
skills2 = {"AI", "Cyber Security", "Gaming"}

skills1.add("Git")
skills1.remove("Python")

print("Union:", skills1.union(skills2))
print("Intersection:", skills1.intersection(skills2))