# Conditions
# if-else
age = 27

if age >= 18 :
    print("adult")
else:
    print("minor")

# if-elif-else
marks = 39

if marks>=90:
    print("AA")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
elif marks>=40:
    print("E")
else:
    print("Fall")

# one-line
status = "Adult" if age >= 18 else "Minor"
print(status)

# nested-loops
hasId = False

if(age>=18):
    if(hasId):
        print("Entry allowed")
    else:
        print("Id required")
else :
    print("Under-age")


# match-case
day = 11
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednusday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")