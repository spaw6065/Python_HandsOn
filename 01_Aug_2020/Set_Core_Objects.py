set1 = {1,2,3,4,5,6,9}
set2 = {5,6,7,8}

print("set1", set1)
print("set2", set2)

# set1.remove(1)
# print(set1)
#
# set1.add("ethans")
# print(set1)
#
# set1.discard(-5)
# print(set1)

##union
print("Union",set1.union(set2))
print("Difference",set1.difference(set2))
print("Intersect",set1.intersection(set2))
print(set1)
set1.difference_update(set2)
print(set1)
print(set2)

##symmetric
s5={1,2,3,4,5,6,7}
s6={5,6,7,8,9,0}

print("symmetric_Diff",s5.symmetric_difference(s6))
print("s5",s5)

s5.symmetric_difference_update(s6)
print("s5 2",s5)

set6 = {1,2,3,4,5,6,7}
subset6={0}

print("Is subset",subset6.issubset(set6))
print("Is superset",set6.issuperset(subset6))

##Returns true if no intersecting elements present
print("disjoint",set6.isdisjoint(subset6))
