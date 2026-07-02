# Dictionary (use case: JSON, APIs, databases, ML)
user = {
    "name" : "Gourab",
    "age" : 21
}
print(user)
print("user name is ",user["name"])

# type
print("The user type is ", type(user))

# value update
user["city"] = "Kolkata"
print(user)

user["age"] = 22
print(user["age"])

# .get()
print("My name is",user.get("name"))
# return none or change according to dev if it's not exist
print("My email id is", user.get("email"))
print("My email id is", user.get("email", "Not Found"))

# .keys()
print(user.keys())

for key in user.keys():
    print("user key is",key)


# .values()
print(user.values())
for val in user.values():
    print("value is ", val)

# .items()
print(user.items())
for key, val in user.items():
    print("key is", key, "and value is", val)

# .update()
user.update({
    "email": "abc@gmail.com"
})
print(user)

# .pop()
user.pop("city")
print(user)

user2 = user
print(user2)

# size
print("size of user is",len(user))

# .clear()
print(user)
user.clear()
print("after clear:", user)

# Nested Dictionary
student = {
    "name" : "Gourab Das",
    "roll" : 1020,
    "marks" : {
        "ben" : 74,
        "eng" : 79,
        "phy" : 87,
        "chem" : 93,
        "math" : 83
    },
    "grade" : "B"
}
print(student)
print(student["marks"]["ben"])
print("Marks of", student["name"], "in math :",student["marks"]["math"])


