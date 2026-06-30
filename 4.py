# loop control statements
# Break
for i in range(10):
    if i==3:
        break
    print(i)

# continue
for i in range(5):
    if i==2:
        continue
    print(i)

# pass     // do nothing
for i in range(5):
    if i==2 :
        pass
    print(i)

# else with Loops
for i in range(5):
    print("Gourab Das", i)
else:
    print("Loop Completed")