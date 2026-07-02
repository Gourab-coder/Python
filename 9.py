# Set (Removing duplicates, fast lookup)
# A set is an unordered collection of unique elements.

nums1 = {1, 2, 3, 4}
print(nums1)

# type
print(type(nums1))

# remove duplicates
nums2 = {1, 4, 8, 6, 4, 1, 3, 1, }
print(nums2)

# creates an empty dictionarset
st = set()
print(type(st))
print(st)
print(len(st))

# .add()
st.add(4)
st.add(1)
st.add(7)
st.add(3)
st.add(1)
st.add(9)
st.add(11)
print(st)

# .pop()  (depending on the set's internal order, because set is unordered)
print("st before pop()", st)
st.pop()
print("st after pop()", st)

# .remove()
st.remove(3)
print("after removing 3 :", st)

# if not exist X throw error: KeyError: X
# st.remove(10)

# .discard()
st.discard(1)
print("after discard 1 is :", st)

# discard never throw any error
st.discard(10)


A = {1, 2, 3}
B = {2, 3, 4, 5}

# .union()  (throw all unique elments from A and B) // 1, 2, 3, 4, 5
print(A.union(B))

# .intersection()  (throw all common elments from A and B) // 2, 3
print(A.intersection(B))

# .difference() (throw all uncommon elments of A with B) // 1
print(A.difference(B))

# .copy()
c = A.copy()
print(c)

# .clear()
c.clear()
print(c)




