# Dictionaries

# key value pairs

# key is the reference. Value is the data stored.

# Making a dictionary

student_1 = {
    "name":"zain",
    "stream":"devops",
    "completed_lessons":4,
    "completed_lesson_names":["variables","git","data_types","collections"]

}

print(type(student_1))

# How to acess parts of a dictionary

print(student_1["name"])
print(student_1["completed_lesson_names"][:1])

# changing a value

student_1["completed_lessons"] = 3
print(student_1)

student_1["completed_lesson_names"].remove("data_types")
print(student_1)

# dictionary methods

print(student_1.keys())
print(student_1.values())

