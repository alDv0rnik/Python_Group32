# CLEAR
students = {"name": "Nick", "age": 19, "course": "Python"}
# students.clear()
# print(students)

# GET
print(students["name"])
print(students.get("name1", {}))

key = "last_name"
if key not in students:
    students[key] = "Smith"
    print(students)
else:
    print(students[key])

# DELETE
del students[key]
print(students)

val = students.pop("name")
print(val)
print(students)

val1 = students.popitem()
print(val1)
print(students)

# SETDEFAULT

students.setdefault("last_name", "Smith")
students.setdefault("last_name", "Doe")
print(students)

keys = students.keys()
print(keys)