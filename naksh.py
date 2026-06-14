# given a list of tuples with info(name , subject):
# .list all unique course
# .list students enrolled in english
# .create dictionary (students, set of courses)
# list of tuples: 

info = [
    ("alice" , "maths"),
    ("bob" , "science"),
    ("alice" , "science"),
    ("charlie" , "maths"),
    ("bob" , "maths"),
    ("alice" , "english"),
    ("charlie" , "english"),
]

# list of unique course

# yaha hum ek set banayenge courses ka usme info ko store karwayenge jisse extra elements remove ho jayenge
unique_courses = set()

for name , courses in info:
    unique_courses.add(courses)
    
print(unique_courses)

