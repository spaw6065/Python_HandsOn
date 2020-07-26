thisdict={
     "Id":1001,
    "name":"Sumit",
    "age":31
}

print(thisdict)
print(thisdict["Id"])
print(thisdict.values())

for x in thisdict:
    print(x)

thisdict.pop("Id")
print(thisdict)

thisdict["Id"]=1001

print(thisdict)
del(thisdict)